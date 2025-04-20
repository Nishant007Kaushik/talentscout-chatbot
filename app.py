import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Title
st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon=":robot_face:")
st.title("TalentScout Hiring Assistant Chatbot")

# Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {
        "name": "",
        "email": "",
        "phone": "",
        "experience": "",
        "position": "",
        "location": "",
        "tech_stack": ""
    }
if "stage" not in st.session_state:
    st.session_state.stage = "start"

# Define stages in order
fields = ["name", "email", "phone", "experience", "position", "location", "tech_stack"]
prompts = {
    "name": "Please enter your full name:",
    "email": "Enter your email address:",
    "phone": "Enter your phone number:",
    "experience": "How many years of experience do you have?",
    "position": "What position are you applying for?",
    "location": "Where are you currently located?",
    "tech_stack": "Please list your tech stack (e.g. Python, React, MySQL):"
}

# Greeting
if st.session_state.stage == "start":
    st.markdown("""
        Hello! I'm your AI Hiring Assistant at TalentScout. 
        I'm here to help with your initial screening process. Let's begin!
    """)
    st.session_state.stage = fields[0]

# Chat Interface
user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.messages.append(("user", user_input))

    # Check for exit keyword
    if any(word in user_input.lower() for word in ["bye", "exit", "quit"]):
        st.markdown("Thank you for your time! We’ll get back to you shortly.")
        st.session_state.stage = "done"
    elif st.session_state.stage in fields:
        st.session_state.candidate_info[st.session_state.stage] = user_input
        current_index = fields.index(st.session_state.stage)
        if current_index + 1 < len(fields):
            st.session_state.stage = fields[current_index + 1]
        else:
            st.session_state.stage = "questions"
    elif st.session_state.stage == "questions":
        tech_stack = st.session_state.candidate_info["tech_stack"]
        prompt = (
            f"Generate 3-5 technical interview questions to evaluate a candidate's skill in: {tech_stack}."
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        questions = response["choices"][0]["message"]["content"]
        st.session_state.messages.append(("assistant", questions))
        st.session_state.stage = "done"
    elif st.session_state.stage == "done":
        st.markdown("You’ve completed the screening! Thank you.")

# Display Assistant Message or Prompt
if st.session_state.stage in fields:
    st.markdown(f"**Assistant:** {prompts[st.session_state.stage]}")

# Display Chat History
st.markdown("---")
for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Assistant:** {msg}")
