from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# for text only prompts
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    # generate content is used to generate text response
    response = model.generate_content(question)
    return response.text

# steamlit

st.set_page_config(page_title="q and a demo")

st.header("Gemini LLM App")

input=st.text_input("Input:", key="input")
submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("Response")
    st.write(response)