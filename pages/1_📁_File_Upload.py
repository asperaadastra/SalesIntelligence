import streamlit as st
import pandas as pd
import base64

st.markdown('<div class="upload-page-pattern">', unsafe_allow_html=True)

# Load your main CSS
def load_css_file(file_path="styles/default.css"):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file()

# Your page content
st.title("📁 Upload Sales Data")
uploaded = st.file_uploader("Upload your CSV file", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.session_state["raw_df"] = df
    st.success("File uploaded!")
    st.dataframe(df.head())