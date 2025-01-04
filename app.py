import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables
load_dotenv()
my_api_key = os.getenv("GOOGLE_API_KEY")

# Configure Generative AI model
genai.configure(api_key=my_api_key)
model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")

# Streamlit interface
st.title("Generative AI with Gemini")
st.write("Ask the AI anything!")

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Input from user
user_input = st.text_input("Enter your query:", "")

if st.button("Generate Response"):
    if user_input:
        response = model.generate_content(user_input)
        st.write(f"**Response:** {response.text}")
        
        # Add query and response to history
        st.session_state.history.insert(0, {"query": user_input, "response": response.text})
    else:
        st.write("Please enter a query.")

# Display history 
if st.session_state.history:
    st.write("## Query History (Latest First)")
    for i, entry in enumerate(st.session_state.history, 1):
        st.write(f"**{i}. Query:** {entry['query']}")
        st.write(f"**Response:** {entry['response']}")
