import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

# AI imports
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

def init():



    st.set_page_config(
        page_title="HealthMate Chat ⚕️",
        page_icon="🏥",
        initial_sidebar_state="expanded",
    )
    load_dotenv()

    # Test that the API key exists
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        st.error("OPENAI_API_KEY is not set. Please set it in your environment.")
        st.stop()
    else:
        st.success("OPENAI_API_KEY is set")


    # Initialize session state
    if "health_data" not in st.session_state:
        st.session_state["health_data"] = {
            "Heart Rate": 80.0,
            "Temperature": 98.6,
        }

def on_button_click():
    pass

def ai_chat():
    st.title("HealthMate Chat 👨‍⚕️")
    st.markdown('---')

    chat = ChatOpenAI()

    # Initialize message history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are the best doctor; you can answer any question asked to you. you also like to give advice to your patients based on their health data."),
        ]

    with st.sidebar:
        user_input = st.text_input("Your message: ", key="user_input")

        if st.button("Send"):
            #Add health data to user input
            user_input += "\nHere are my vitals:\n"
            vitals = st.session_state["health_data"]
            for key in vitals:
                user_input += f"{key}: {vitals[key]}\n"

            user_input += "\nuse this data to answer my question\n"


            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Thinking..."):
                try:
                    response = chat(st.session_state.messages)
                    st.session_state.messages.append(AIMessage(content=response.content))
                except Exception as e:
                    st.error(f"Error generating AI response: {str(e)}")

        # Give 2 options: one to enter health data manually and one to read from Arduino
        health_data_method = st.selectbox("How do you want to enter your health data?", ("Enter Manually", "Read from Arduino"))
        if health_data_method == "Enter Manually":
            # Get all the health data; use keys from dict
            for key in st.session_state["health_data"]:
                # Take input for each key
                st.session_state["health_data"][key] = st.number_input(label=key, value=float(st.session_state["health_data"][key]))

        elif health_data_method == "Read from Arduino":
            # Read from Arduino
            pass

        # Add field
        st.markdown("---")
        st.markdown("### Add Field")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name").capitalize()
        with col2:
            value = st.text_input("Value")
        if st.button("Add"):
            # Get keys from dict
            names = st.session_state["health_data"].keys()
            if name in names:
                st.error("Field already exists")
            else:
                st.session_state["health_data"][name] = value
                st.experimental_rerun()

        # Remove field
        st.markdown("---")
        st.markdown("### Remove Field")

        name = st.selectbox("Name", list(st.session_state["health_data"].keys()))

        if st.button("Remove"):
            del st.session_state["health_data"][name]
            st.experimental_rerun()
        
    chat_placeholder = st.empty()
    with chat_placeholder.container():
        messages = st.session_state.get('messages', [])
        for i, msg in enumerate(messages[1:]):
            if i % 2 == 0:
                message(msg.content, is_user=True, key=str(i) + '_user')
            else:
                message(msg.content, is_user=False, key=str(i) + '_ai')

def main():
    init()
    ai_chat()

if __name__ == "__main__":
    main()
