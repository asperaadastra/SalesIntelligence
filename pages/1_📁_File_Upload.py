import streamlit as st
import pandas as pd

# DIRECT CSS INJECTION - This will definitely work
st.markdown("""
<style>
/* ----------------------------- */
/* BACKGROUND PATTERN - SIMPLE AND VISIBLE */
/* ----------------------------- */
.stApp {
    background: 
        linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.95)),
        repeating-linear-gradient(
            45deg,
            #000000 0px,
            #000000 2px,
            transparent 2px,
            transparent 10px
        ) !important;
}

/* ----------------------------- */
/* BASIC STYLING */
/* ----------------------------- */
body {
    font-family: "Inter", sans-serif !important;
    color: #2c3e50 !important;
}

h1 {
    background: linear-gradient(135deg, #0099b5, #1e8e3e, #ce1126) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    text-align: center !important;
    font-size: 2.5em !important;
    padding: 20px !important;
    border: 3px solid #0099b5 !important;
    border-radius: 15px !important;
    margin: 20px 0 !important;
}

/* File uploader */
.stFileUploader > div {
    background: white !important;
    border: 3px dashed #0099b5 !important;
    border-radius: 15px !important;
    padding: 40px !important;
    text-align: center !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #0099b5, #1e8e3e) !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 15px 30px !important;
    border: none !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* Success message */
.stSuccess {
    background: #1e8e3e !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 20px !important;
    text-align: center !important;
}

/* Containers */
.stMarkdown, .stDataFrame {
    background: white !important;
    padding: 20px !important;
    border-radius: 10px !important;
    border: 2px solid #0099b5 !important;
    margin: 10px 0 !important;
}
</style>
""", unsafe_allow_html=True)

# Your page content
st.title("📁 Upload Sales Data")

uploaded = st.file_uploader("Upload your CSV file", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.session_state["raw_df"] = df
    st.success("File uploaded successfully!")
    st.dataframe(df.head())
    
    # Show file info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Rows", len(df))
    with col2:
        st.metric("Columns", len(df.columns))
    with col3:
        st.metric("File Size", f"{uploaded.size / 1024:.1f} KB")