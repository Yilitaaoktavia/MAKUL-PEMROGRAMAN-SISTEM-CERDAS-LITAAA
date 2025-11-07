import google.generativeai as genai
import streamlit as st

# konfigurasi API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# panggil model yang benar
model = genai.GenerativeModel("gemini pro")

# tes isi prompt
response = model.generate_content("Hai, aku Yilita! Apa kabar?")
st.write(response.text)
