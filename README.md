## TalentScout Chatbot 🧠💼

**TalentScout** is an AI-powered hiring assistant chatbot built with **Streamlit** and **OpenAI’s language models**. Designed to simplify and enhance the candidate screening process, this chatbot interacts with the user to gather a required tech stack and intelligently evaluates candidate profiles based on their relevance.

---

## 📌 Key Features

- ✅ **LLM-Based Candidate Screening**: Uses OpenAI’s GPT models to assess whether candidates meet technical requirements.
- 🧾 **User-Friendly Interface**: Built with Streamlit for easy use by HR professionals and recruiters.
- 🔍 **Input-Based Matching**: You provide a list of required technologies or skills, and the bot analyzes candidate suitability.
- 🔐 **Secure Credential Handling**: API keys are stored securely using `.streamlit/secrets.toml`.
- ☁️ **Deployable to Streamlit Cloud**: Fast and easy deployment with no need for backend setup.

---

## 📁 Project Structure

talentscout-chatbot/
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── .streamlit/
│   ├── config.toml
├── utils/
│   ├── helper.py
│   ├── model_utils.py
├── assets/
│   ├── logo.png
├── data/
│   ├── sample_resume.pdf
├── models/
│   ├── candidate_match_model.pkl
