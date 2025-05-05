# 💬 Gemini Chatbot App

A fully interactive chatbot interface built using **Streamlit**, powered by **Google's Gemini Pro (1.5 Flash)** via the official `google-generativeai` SDK. This app allows real-time AI-powered conversations with adjustable creativity, chat persistence, and a clean, responsive design.


## ✨ Features

✅ **Conversational Memory**  
Maintains context-aware interactions using Gemini's `start_chat()` with history.

✅ **Adjustable Temperature**  
Choose how creative or deterministic the model should behave (0.0–1.0 scale).

✅ **Chat History with Timestamps**  
Each user and model message is saved with real-time timestamps.

✅ **Secure API Key Handling**  
Uses environment variables via `dotenv` for secure API key management.

✅ **Clear Chat Button**  
Easily reset the conversation from the sidebar.

✅ **Modern UI & Footer**  
Clean layout with a custom developer footer including GitHub and LinkedIn links.


## 🛠️ Built With

| Technology             | Purpose                                      |
|------------------------|----------------------------------------------|
| `Python`               | Core programming language                    |
| `Streamlit`            | UI framework for deploying ML/web apps       |
| `google-generativeai` | Gemini API SDK from Google                   |
| `dotenv`               | Secure API key management (.env loading)     |
| `datetime`             | Timestamps for messages                      |


## 🔐 Prerequisites

Before running the app, ensure the following:

- Python 3.8 or higher is installed
- A valid **Gemini API key** from [Google AI Studio](https://makersuite.google.com/app)


## 🧪 Local Setup Instructions
- streamlit run app.py

## 🧑‍💻 Developers & Credits

- Built By:

- **Syed Haider Abbas Zaidi**  
  [GitHub](https://github.com/haider14-9abbaas) | [LinkedIn](https://www.linkedin.com/in/syed-haider-abbas-zaidi-132525215/)

- **Abdul Basit**  
  [GitHub](https://github.com/basitkk48) | [LinkedIn](https://www.linkedin.com/in/abdul-basit-kk-554012309)


