from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# for impage  prompts
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text
    
# steamlit

st.set_page_config(page_title="q and a demo")

st.header("Gemini LLM App")

input=st.text_input("Input:", key="input")

uploaded_file = st.file_uploader("Choose image", type = ["jpg","jpeg"])
image=""
if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image", use_column_width=True)


submit =st.button("TEll me about image")

response = get_gemini_response(input,image)
st.subheader("Response")
st.write(response)