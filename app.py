import streamlit as st
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)


# ✅ Set page config
st.set_page_config(page_title="Gemini Chat", page_icon="💬", layout="centered")
st.title("💬 Chat with Gemini")
st.caption("Powered by Google Gemini | Type `exit` to end the chat.")

# ✅ Model temperature slider
temperature = st.sidebar.slider("🧠 Model Creativity (Temperature)", 0.0, 1.0, 0.5, 0.1)

# ✅ Chat initialization
if "chat" not in st.session_state:
    st.session_state.chat = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"temperature": temperature}
    ).start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Clear chat button
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.chat = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"temperature": temperature}
    ).start_chat(history=[])
    st.session_state.messages = []
    st.rerun()

# ✅ Show message history
for msg in st.session_state.messages:
    timestamp = msg["time"].strftime("%H:%M:%S")
    if msg["role"] == "user":
        st.markdown(f"🧑 **You** ({timestamp}): {msg['text']}")
    else:
        st.markdown(f"🤖 **Gemini** ({timestamp}):")
        st.markdown(msg["text"], unsafe_allow_html=True)

# ✅ Input form to avoid reruns on typing
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message:")
    submitted = st.form_submit_button("Send")

# ✅ Input handling
if submitted and user_input:
    if user_input.strip().lower() == "exit":
        st.success("👋 Chat ended. Refresh to start a new session.")
        st.stop()

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "text": user_input,
        "time": datetime.now()
    })

    try:
        # Send message to Gemini
        response = st.session_state.chat.send_message(user_input)
        bot_reply = response.text

        # Save Gemini response
        st.session_state.messages.append({
            "role": "model",
            "text": bot_reply,
            "time": datetime.now()
        })

        st.rerun()


    except Exception as e:
        st.error(f"❌ Error: {e}") #streamlit run gemini_chat_app.py

st.markdown("""
<style>
.dev-footer {
    text-align: center;
    margin-top: 50px;
    padding: 20px 10px;
    font-family: 'Segoe UI', sans-serif;
    color: #4a4a4a;
}
.dev-footer .names {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 10px;
}
.dev-footer .icon-row {
    display: flex;
    justify-content: center;
    gap: 60px;
    flex-wrap: wrap;
    margin-top: 10px;
}
.dev-footer .person {
    text-align: center;
}
.dev-footer a {
    margin: 0 8px;
    text-decoration: none;
    transition: transform 0.2s;
}
.dev-footer a:hover {
    transform: scale(1.2);
}
.dev-footer svg {
    width: 28px;
    height: 28px;
    vertical-align: middle;
}
</style>

<div class="dev-footer">
    <div class="names">Developed By <br> Syed Haider Abbas Zaidi & Abdul Basit </div>
    <div class="icon-row">
        <div class="person">
            <a href="https://github.com/haider14-9abbaas" target="_blank" title="Syed's GitHub">
                <svg role="img" viewBox="0 0 24 24" fill="black" xmlns="http://www.w3.org/2000/svg">
                    <title>GitHub</title>
                    <path d="M12 0C5.37 0 0 5.373 0 12c0 5.303 
                    3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 
                    0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61
                    -.546-1.387-1.333-1.757-1.333-1.757-1.09-.745.083-.729.083-.729 
                    1.205.084 1.84 1.236 1.84 1.236 1.07 1.834 2.807 1.304 3.492.997.108-.775.418-1.305.76-1.605
                    -2.665-.3-5.467-1.334-5.467-5.93 0-1.31.467-2.38 1.235-3.22 
                    -.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23a11.51 
                    11.51 0 0 1 3.003-.403c1.02.005 2.045.138 3.003.403 
                    2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 
                    3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.807 
                    5.625-5.48 5.92.42.36.81 1.096.81 2.22 
                    0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 
                    21.795 24 17.295 24 12c0-6.627-5.373-12-12-12Z"/>
                </svg>
            </a>
            <a href="https://www.linkedin.com/in/syed-haider-abbas-zaidi-132525215/" target="_blank" title="Syed's LinkedIn">
                <svg role="img" viewBox="0 0 24 24" fill="#0A66C2" xmlns="http://www.w3.org/2000/svg">
                    <title>LinkedIn</title>
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.327-.027-3.037-1.852-3.037-1.853 
                    0-2.136 1.445-2.136 2.939v5.667H9.352V9h3.414v1.561h.049c.476-.9 
                    1.637-1.852 3.37-1.852 3.599 0 4.267 2.368 4.267 5.452v6.291zM5.337 
                    7.433a2.062 2.062 0 1 1 0-4.123 2.062 2.062 0 0 1 0 
                    4.123zm1.777 13.019H3.56V9h3.554v11.452zM22.225 
                    0H1.771C.792 0 0 .774 0 1.729v20.542C0 
                    23.225.792 24 1.771 24h20.451C23.2 24 
                    24 23.225 24 22.271V1.729C24 .774 23.2 0 
                    22.222 0h.003z"/>
                </svg>
            </a>
        </div>
        <div class="person">
            <a href="https://github.com/basitkk48" target="_blank" title="Basit's GitHub">
                <svg role="img" viewBox="0 0 24 24" fill="black" xmlns="http://www.w3.org/2000/svg">
                    <title>GitHub</title>
                    <path d="M12 0C5.37 0 0 5.373 0 12c0 5.303 
                    3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 
                    0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61
                    -.546-1.387-1.333-1.757-1.333-1.757-1.09-.745.083-.729.083-.729 
                    1.205.084 1.84 1.236 1.84 1.236 1.07 1.834 2.807 1.304 3.492.997.108-.775.418-1.305.76-1.605
                    -2.665-.3-5.467-1.334-5.467-5.93 0-1.31.467-2.38 1.235-3.22 
                    -.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23a11.51 
                    11.51 0 0 1 3.003-.403c1.02.005 2.045.138 3.003.403 
                    2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 
                    3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.807 
                    5.625-5.48 5.92.42.36.81 1.096.81 2.22 
                    0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 
                    21.795 24 17.295 24 12c0-6.627-5.373-12-12-12Z"/>
                </svg>
            </a>
            <a href="https://www.linkedin.com/in/abdul-basit-kk-554012309?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank" title="Basit's LinkedIn">
                <svg role="img" viewBox="0 0 24 24" fill="#0A66C2" xmlns="http://www.w3.org/2000/svg">
                    <title>LinkedIn</title>
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.327-.027-3.037-1.852-3.037-1.853 
                    0-2.136 1.445-2.136 2.939v5.667H9.352V9h3.414v1.561h.049c.476-.9 
                    1.637-1.852 3.37-1.852 3.599 0 4.267 2.368 4.267 5.452v6.291zM5.337 
                    7.433a2.062 2.062 0 1 1 0-4.123 2.062 2.062 0 0 1 0 
                    4.123zm1.777 13.019H3.56V9h3.554v11.452zM22.225 
                    0H1.771C.792 0 0 .774 0 1.729v20.542C0 
                    23.225.792 24 1.771 24h20.451C23.2 24 
                    24 23.225 24 22.271V1.729C24 .774 23.2 0 
                    22.222 0h.003z"/>
                </svg>
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
