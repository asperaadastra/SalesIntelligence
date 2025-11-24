import streamlit as st
import hashlib

def load_css_file(file_path="styles/default.css"):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file()

st.set_page_config(page_title="Grocery ML App", page_icon="🛒", layout="wide")

# Simple login system
def login():
    st.title("🛒 Grocery Sales Dashboard - Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # simple password hashing
    def hash_pw(pw):
        return hashlib.sha256(pw.encode()).hexdigest()

    users = {
        "admin": hash_pw("1234"),
        "demo": hash_pw("demo")
    }

    if st.button("Login"):
        if username in users and users[username] == hash_pw(password):
            st.session_state["logged_in"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()

st.write("Welcome to the Grocery Store ML app! Use the sidebar to navigate pages.")
