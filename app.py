# app.py
import streamlit as st
import pandas as pd
import openai
from utils import classify_dispute

st.set_page_config(page_title="FinGPT Dispute Assistant", layout="centered")
st.title("📈 FinGPT Dispute Assistant")

st.markdown("""
Enter a customer dispute below. The assistant will classify the issue,
suggest a resolution, and generate a summary for internal teams.
""")

openai.api_key = st.secrets["OPENAI_API_KEY"]

user_input = st.text_area("Paste Customer Dispute", height=200)

if st.button("Analyze Dispute") and user_input:
    with st.spinner("Analyzing with GPT..."):
        classification, resolution, summary = classify_dispute(user_input)

    st.subheader("Issue Classification")
    st.write(classification)

    st.subheader("Suggested Resolution")
    st.write(resolution)

    st.subheader("Summary for Internal Team")
    st.success(summary)

st.markdown("---")
st.markdown("*Note: This is a sample tool using GPT-4 for demonstration only.*")
