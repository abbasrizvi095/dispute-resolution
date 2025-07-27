# utils.py
import openai
from prompts import build_prompt

client = openai.OpenAI()  # Uses API key from .streamlit/secrets.toml

def classify_dispute(dispute_text):
    prompt = build_prompt(dispute_text)

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # ✅ Replace "gpt-4" with this
    messages=[{"role": "user", "content": prompt}],
    temperature=0.4,
)


    output = response.choices[0].message.content.strip()

    try:
        lines = output.strip().split("\n")
        classification = lines[0].split(":", 1)[1].strip()
        resolution = lines[1].split(":", 1)[1].strip()
        summary = lines[2].split(":", 1)[1].strip()
        return classification, resolution, summary
    except:
        return "Could not parse", "-", output
