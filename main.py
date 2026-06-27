import os
import json
import requests

from dotenv import load_dotenv

from tools import calculate_bmi
from tools import calculate_age
from tools import calculate_grade

from memory import load_memory, save_memory
from prompts import SYSTEM_PROMPT

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "openai/gpt-oss-20b:free"

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

####################################################
# TOOLS
####################################################

TOOLS = [

{
"type":"function",
"function":{
"name":"calculate_bmi",
"description":"Calculate BMI from weight and height.",
"parameters":{
"type":"object",
"properties":{
"weight":{
"type":"number",
"description":"Weight in kilograms"
},
"height":{
"type":"number",
"description":"Height in meters"
}
},
"required":["weight","height"]
}
}
},

{
"type":"function",
"function":{
"name":"calculate_age",
"description":"Calculate age from birth year.",
"parameters":{
"type":"object",
"properties":{
"birth_year":{
"type":"integer",
"description":"Birth year"
}
},
"required":["birth_year"]
}
}
},

{
"type":"function",
"function":{
"name":"calculate_grade",
"description":"Calculate grade from marks.",
"parameters":{
"type":"object",
"properties":{
"mark":{
"type":"number",
"description":"Student marks"
}
},
"required":["mark"]
}
}
}

]

####################################################
# TOOL MAPPING
####################################################

TOOL_FUNCTIONS = {

"calculate_bmi": calculate_bmi,

"calculate_age": calculate_age,

"calculate_grade": calculate_grade

}

####################################################
# CALL LLM
####################################################

def call_llm(messages):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "tools": TOOLS
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload
    )

    response.raise_for_status()

    return response.json()

####################################################
# RUN TOOL
####################################################

def run_tool(tool_call):

    tool_name = tool_call["function"]["name"]

    tool_args = json.loads(
        tool_call["function"]["arguments"]
    )

    if tool_name in TOOL_FUNCTIONS:

        result = TOOL_FUNCTIONS[tool_name](**tool_args)

        return str(result)

    return "Tool not found."

####################################################
# AGENT LOOP
####################################################

def agent_loop(user_input):

    memory = load_memory()

    messages = [
        {
            "role":"system",
            "content":SYSTEM_PROMPT
        }
    ]

    messages.extend(memory)

    messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )

    for _ in range(5):

        result = call_llm(messages)

        message = result["choices"][0]["message"]

        messages.append(message)

        if "tool_calls" in message and message["tool_calls"]:

            for tool_call in message["tool_calls"]:

                tool_result = run_tool(tool_call)

                messages.append({
                    "role":"tool",
                    "tool_call_id":tool_call["id"],
                    "name":tool_call["function"]["name"],
                    "content":tool_result
                })

        else:

            final_answer = message.get("content")

            save_memory(messages[1:])

            return final_answer

    return "Maximum steps reached."

####################################################
# MAIN
####################################################

if __name__ == "__main__":

    print("===== Utility Agent =====")

    print("Available Utilities")

    print("1. BMI Calculator")

    print("2. Age Calculator")

    print("3. Grade Calculator")

    print()

    while True:

        user = input("You: ")

        if user.lower() == "exit":
            break

        try:

            response = agent_loop(user)

            print("\nAgent:", response)
            print()

        except Exception as e:

            print(e)