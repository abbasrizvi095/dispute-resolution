# app.py
import streamlit as st
import pandas as pd
import openai
from utils import classify_dispute
from entityRecognitionUtils import extract_entities
from search_utils import search_similar_disputes
from auto_routing import get_routing_team

st.set_page_config(page_title="Online Dispute Assistant", layout="centered")
st.title("📈 Online Dispute Resolution Assistant")

st.markdown("""
Enter a customer dispute below. The assistant will help to classify the issue,
suggest a suitable resolution, and generate a summary for internal teams.
""")

openai.api_key = st.secrets["OPENAI_API_KEY"]

user_input = st.text_area("Paste Customer Dispute", height=200)

classification = None

if st.button("Analyze Dispute") and user_input:
    with st.spinner("Analyzing the dispute..."):
        classification, resolution, summary = classify_dispute(user_input)

    st.subheader("Dispute Classification")
    st.write(classification)

    st.subheader("Suggested Resolution")
    st.write(resolution)

    st.subheader("Summary for Internal Team")
    st.success(summary)

# Add a section for search
    with st.spinner("Searching similar disputes..."):
            similar_results = search_similar_disputes(user_input)

    st.subheader("🔍 Similar Past Disputes")
    if similar_results is not None and not similar_results.empty:
        for idx, row in similar_results.head(3).iterrows():
            st.markdown(f"**Dispute ID:** {row['DisputeID']}  ")
            st.markdown(f"**Text:** {row['DisputeText']}")
            st.markdown("---")
    else:
        st.write("No similar disputes found.")

# Obtain named entities
st.subheader("Named Entities (NER)")
entities = extract_entities(user_input)
if entities:
    for entity_text, label in entities:
         st.markdown(f"- **{label}**: {entity_text}")
else:
    st.info("No named entities found.")

# After classification output:
routing_team = get_routing_team(classification)
st.subheader("Routing Suggestion")
st.info(f"Route to: {routing_team}")

st.markdown("---")
st.markdown("*Note: This is a sample tool using GPT API for demonstration.*")