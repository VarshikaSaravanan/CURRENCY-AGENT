# Currency AI Agent

## Overview

The Currency AI Agent is a Python-based intelligent assistant that provides real-time currency exchange information using the OpenRouter API and an external exchange rate service. The application is designed to answer only currency-related queries by utilizing AI function calling and live data retrieval instead of generating estimated responses.

The project demonstrates the implementation of AI agents, tool calling, prompt engineering, conversation memory, and API integration in Python.
<img width="1143" height="512" alt="image" src="https://github.com/user-attachments/assets/4f9e3962-2293-4b4f-8c18-3def287dcb30" />


---

## Features

- Real-time currency exchange rate retrieval
- Currency conversion between multiple currencies
- AI-powered responses using the OpenRouter API
- Function (Tool) Calling for live data retrieval
- Conversation memory using JSON
- Environment variable support for secure API key management
- Command-line interface for user interaction

---

## Technologies Used

- Python 3.x
- OpenRouter API
- Exchange Rate API
- Requests
- Python Dotenv
- JSON

---

## Project Structure

```
Currency-Exchange-AI-Agent/
│
├── main.py              # Main application
├── tools.py             # Currency tool functions
├── prompts.py           # AI system prompt
├── memory.py            # Conversation memory functions
├── memory.json          # Stores previous conversations
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Currency-Exchange-AI-Agent.git
cd Currency-Exchange-AI-Agent
```

### Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project directory.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

## Running the Application

```bash
python main.py
```

---

## Sample Interaction

```
==========================
 Currency AI Agent
==========================

You : What is the exchange rate from USD to INR?

Agent :

Exchange Rate

From:
USD

To:
INR

Rate:
1 USD = 86.24 INR
```

---

## How It Works

1. The user submits a currency-related query.
2. The AI agent sends the request to the OpenRouter language model.
3. If live exchange rate information is required, the model invokes the appropriate tool.
4. The tool retrieves the latest exchange rate from the external API.
5. The result is returned to the user.
6. Conversation history is stored locally for maintaining context.

---

## Supported Queries

Examples include:

- What is the exchange rate from USD to INR?
- Convert 100 USD to EUR.
- What is the currency code of Japan?
- What is the currency symbol of India?
- Exchange rate between GBP and AUD.

---

## Dependencies

The project requires the following Python packages:

```
requests
python-dotenv
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## Project Components

### main.py

- Handles user interaction
- Communicates with the OpenRouter API
- Processes tool calls
- Controls the agent workflow

### tools.py

Provides functions for:

- Retrieving exchange rates
- Currency conversion

### prompts.py

Contains the system prompt that restricts the AI agent to currency-related tasks.

### memory.py

Implements persistent conversation storage using a JSON file.

---

## Future Enhancements

- Graphical User Interface (GUI)
- Web application using Flask or Streamlit
- Historical exchange rate analysis
- Multi-language support
- Cryptocurrency exchange support
- Voice-enabled interaction

---

## Learning Outcomes

This project demonstrates practical implementation of:

- AI Agents
- Prompt Engineering
- Function Calling
- REST API Integration
- Environment Variable Management
- JSON Data Handling
- Conversation Memory
- Python Programming

---

## License

This project is developed for educational and learning purposes. It may be modified and extended for personal or academic use.

---

## Author

**Varshika Saravanan**

Bachelor of Technology – Information Technology
