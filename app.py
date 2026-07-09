import streamlit as st
from main import agent_loop
from memory import load_memory

st.set_page_config(page_title="Currency AI Agent", page_icon="💸")

st.title("Currency AI Agent 💸")
st.markdown("Ask me about currency conversions, exchange rates, and currency symbols!")

# Display chat history from memory
memory = load_memory()
for msg in memory:
    if msg["role"] in ["user", "assistant", "tool"]:
        if msg.get("content"):
            # Display tool outputs as assistant messages
            role = "assistant" if msg["role"] == "tool" else msg["role"]
            with st.chat_message(role):
                st.markdown(msg["content"])

if prompt := st.chat_input("What is the currency of India?"):
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Show spinner while agent is thinking
    with st.spinner("Thinking..."):
        try:
            response = agent_loop(prompt)
            with st.chat_message("assistant"):
                st.markdown(response)
        except Exception as e:
            st.error(f"Error: {e}")
