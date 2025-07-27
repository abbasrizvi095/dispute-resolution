# 📈 FinGPT Dispute Assistant

A lightweight AI-powered tool that classifies customer banking disputes, suggests resolution steps, and generates internal summaries using GPT-4.

## 🔄 Use Case
Inspired by real-world internal tools in banking environments (e.g., HSBC), this demo streamlines dispute resolution for operations, compliance, or product teams.

## 💡 Features
- Classifies disputes (e.g., KYC, fraud, transaction issues)
- Suggests internal resolution actions
- Generates summaries for compliance/legal teams

## ⚙️ Stack
- **Frontend**: Streamlit
- **AI**: OpenAI GPT-4
- **Data**: Sample CSV disputes

## 🚀 Getting Started
1. `pip install streamlit openai pandas`
2. Add your OpenAI key: `streamlit secrets set OPENAI_API_KEY="your-key"`
3. Run app: `streamlit run app.py`

## 🌐 Deployment
Use [Streamlit Cloud](https://streamlit.io/cloud) or [HuggingFace Spaces](https://huggingface.co/spaces)

## 🛑 Disclaimer
Demo purpose only. Not for production use.
