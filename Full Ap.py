import streamlit as st
import openai
import os

# === API Setup ===
openai.api_key = st.secrets["OPENAI_API_KEY"]  # safer than hardcoding!

# === App Configuration ===
st.set_page_config(
    page_title="Your Eco Bestie 🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# === Custom Style ===
st.markdown("""
    <style>
        body {
            background-color: #f2f1e9;
            font-family: 'Georgia', serif;
            color: #2d2a26;
        }
        .stTextInput > div > div > input {
            background-color: #fff8f1;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #90a955;
            color: white;
            border-radius: 8px;
        }
        .stMarkdown {
            font-size: 1.05rem;
        }
    </style>
""", unsafe_allow_html=True)

# === Title & Intro ===
st.title("🌿 Your Eco Bestie")
st.markdown("Welcome to your personalized sustainability guide. Ask me anything about eco-friendly living, green swaps, or how to reduce your footprint. I'm here to help 🌎")

# === User Input ===
user_input = st.text_input("💬 What would you like help with today?")

# === Generate AI Response ===
if user_input:
    with st.spinner("Thinking green thoughts... 🌱"):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're a kind, non-judgmental eco-living assistant. Give helpful, friendly answers using natural and sustainable lifestyle tips. Keep answers concise and optionally link to useful resources."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7
            )

            answer = response.choices[0].message.content.strip()
            st.markdown("#### 🌻 Here’s your tip:")
            st.write(answer)

        except Exception as e:
            st.error("Oops, I couldn’t find an answer. Please try again later.")
            st.caption(f"Error: {e}")

# === Footer ===
st.markdown("---")
st.caption("Created with 🌿 by The Eco Connection • Powered by OpenAI & Streamlit")
