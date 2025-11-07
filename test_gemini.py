import streamlit as st
import google.generativeai as genai

# konfigurasi API key dari secrets.toml
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# gunakan model stabil
model = genai.GenerativeModel("gemini-pro")

# uji output
prompt = "Hai, aku Yilita! Apa kabar?"
response = model.generate_content(prompt)

st.title("Tes Gemini API")
st.write(response.text)
