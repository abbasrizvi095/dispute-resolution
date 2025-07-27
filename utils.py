# utils.py
import openai
from prompts import DISPUTE_PROMPT

def classify_dispute(dispute_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful banking dispute assistant."},
            {"role": "user", "content": DISPUTE_PROMPT.format(dispute_text=dispute_text)}
        ],
        temperature=0.3
    )

    result = response.choices[0].message['content']
    try:
        parts = result.split("\n")
        classification = parts[0].replace("Classification:", "").strip()
        resolution = parts[1].replace("Suggested Resolution:", "").strip()
        summary = parts[2].replace("Internal Summary:", "").strip()
        return classification, resolution, summary
    except Exception:
        return "Unknown", "Please review manually.", result
