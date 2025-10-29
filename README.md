# 🚀 LetGen

[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/streamlit-app-orange)](https://streamlit.io/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Generate professional, personalized cover letters in seconds using AI!**  

This **Streamlit web app** uses AI agents and SERP API to analyze your CV, additional documents, and company info, then crafts a tailored cover letter in your preferred tone and length.

---

## 🎯 Features

- **Multi-document input** – Upload CV, recommendations, LinkedIn PDFs, or summaries.  
- **Company & Role focused** – Personalizes letters for the exact job and company.  
- **Customizable tone & length** – Professional, friendly, creative; short, medium, long.  
- **AI-powered candidate profiling** – Extracts all relevant information from your documents.  
- **Web-aware generation** – Retrieves role/company insights from the web using SERP API.  
- **Streamlit interface** – Simple, intuitive UI to generate and download your letter.

---

## ⚡ Quick Start

```bash
# Clone repository
git clone https://github.com/michalwegiel/LetGen.git

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Set API keys
# create .env file with API keys
OPENAI_API_KEY="your_openai_key"
SERPAPI_API_KEY="your_serpapi_key"

# Run app
streamlit run app.py
```
