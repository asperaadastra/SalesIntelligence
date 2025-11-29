import streamlit as st
import pandas as pd

# UZBEK TRADITIONAL PATTERNS - DIRECT CSS INJECTION
st.markdown("""
<style>
/* ----------------------------- */
/* UZBEK IKAT PATTERN BACKGROUND */
/* ----------------------------- */
.stApp {
    background: 
        linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.92)),
        repeating-linear-gradient(
            0deg,
            transparent 0px,
            transparent 20px,
            rgba(0, 153, 181, 0.1) 20px,
            rgba(0, 153, 181, 0.1) 22px,
            transparent 22px,
            transparent 40px,
            rgba(30, 142, 62, 0.1) 40px,
            rgba(30, 142, 62, 0.1) 42px,
            transparent 42px,
            transparent 60px,
            rgba(206, 17, 38, 0.1) 60px,
            rgba(206, 17, 38, 0.1) 62px,
            transparent 62px
        ),
        repeating-linear-gradient(
            90deg,
            transparent 0px,
            transparent 20px,
            rgba(0, 153, 181, 0.08) 20px,
            rgba(0, 153, 181, 0.08) 22px,
            transparent 22px,
            transparent 40px,
            rgba(30, 142, 62, 0.08) 40px,
            rgba(30, 142, 62, 0.08) 42px,
            transparent 42px,
            transparent 60px,
            rgba(206, 17, 38, 0.08) 60px,
            rgba(206, 17, 38, 0.08) 62px,
            transparent 62px
        ) !important;
    background-size: 100% 100% !important;
}

/* ----------------------------- */
/* TRADITIONAL UZBEK STYLING */
/* ----------------------------- */
body {
    font-family: "Inter", "Arial", sans-serif !important;
    color: #2c3e50 !important;
}

/* Main title with traditional borders */
h1 {
    background: linear-gradient(135deg, #0099b5 0%, #1e8e3e 50%, #ce1126 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    text-align: center !important;
    font-size: 2.8em !important;
    font-weight: 800 !important;
    padding: 25px !important;
    margin: 25px 0 !important;
    position: relative !important;
    border: none !important;
}

/* Add traditional pattern to title */
h1::before {
    content: "" !important;
    position: absolute !important;
    top: 0 !important;
    left: 10% !important;
    right: 10% !important;
    height: 4px !important;
    background: linear-gradient(90deg, #0099b5, #1e8e3e, #ce1126) !important;
    border-radius: 2px !important;
}

h1::after {
    content: "" !important;
    position: absolute !important;
    bottom: 0 !important;
    left: 10% !important;
    right: 10% !important;
    height: 4px !important;
    background: linear-gradient(90deg, #ce1126, #1e8e3e, #0099b5) !important;
    border-radius: 2px !important;
}

/* File uploader with traditional design */
.stFileUploader > div {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 255, 240, 0.9)) !important;
    border: 3px dashed #0099b5 !important;
    border-radius: 15px !important;
    padding: 50px 40px !important;
    text-align: center !important;
    position: relative !important;
    backdrop-filter: blur(5px) !important;
}

/* Add pattern to uploader corners */
.stFileUploader > div::before {
    content: "⚜️" !important;
    position: absolute !important;
    top: 10px !important;
    left: 10px !important;
    font-size: 20px !important;
    opacity: 0.6 !important;
}

.stFileUploader > div::after {
    content: "🌿" !important;
    position: absolute !important;
    bottom: 10px !important;
    right: 10px !important;
    font-size: 20px !important;
    opacity: 0.6 !important;
}

.stFileUploader > div:hover {
    border: 3px dashed #ce1126 !important;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(230, 255, 230, 0.95)) !important;
    transform: translateY(-3px) !important;
    transition: all 0.3s ease !important;
}

/* Buttons with traditional motif */
.stButton > button {
    background: linear-gradient(135deg, #0099b5 0%, #1e8e3e 100%) !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 15px 35px !important;
    border: 2px solid #007a99 !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(0, 153, 181, 0.3) !important;
    position: relative !important;
    overflow: hidden !important;
}

.stButton > button::before {
    content: "" !important;
    position: absolute !important;
    top: 0 !important;
    left: -100% !important;
    width: 100% !important;
    height: 100% !important;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent) !important;
    transition: left 0.5s !important;
}

.stButton > button:hover::before {
    left: 100% !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #007a99 0%, #186a2e 100%) !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 25px rgba(0, 122, 153, 0.4) !important;
}

/* Success message with traditional style */
.stSuccess {
    background: linear-gradient(135deg, #1e8e3e, #27ae60) !important;
    color: white !important;
    border: 2px solid #186a2e !important;
    border-radius: 12px !important;
    padding: 25px !important;
    text-align: center !important;
    box-shadow: 0 6px 20px rgba(30, 142, 62, 0.3) !important;
    position: relative !important;
}

.stSuccess::before {
    content: "✅" !important;
    position: absolute !important;
    left: 20px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    font-size: 24px !important;
}

/* Containers with traditional borders */
.stMarkdown, .stDataFrame, .css-1d391kg {
    background: rgba(255, 255, 255, 0.92) !important;
    padding: 25px !important;
    border-radius: 15px !important;
    border: 2px solid #0099b5 !important;
    margin: 20px 0 !important;
    box-shadow: 0 8px 25px rgba(0, 153, 181, 0.15) !important;
    position: relative !important;
    backdrop-filter: blur(3px) !important;
}

/* Add corner decorations to containers */
.stMarkdown::before, .stDataFrame::before {
    content: "" !important;
    position: absolute !important;
    top: -2px !important;
    left: -2px !important;
    right: -2px !important;
    height: 5px !important;
    background: linear-gradient(90deg, #0099b5, #1e8e3e, #ce1126) !important;
    border-radius: 15px 15px 0 0 !important;
}

/* Metric cards */
[data-testid="metric-container"] {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(248, 253, 255, 0.9)) !important;
    padding: 25px !important;
    border-radius: 12px !important;
    border: 2px solid #0099b5 !important;
    box-shadow: 0 6px 20px rgba(0, 153, 181, 0.2) !important;
    text-align: center !important;
    backdrop-filter: blur(2px) !important;
}

[data-testid="metric-container"] > div:first-child {
    font-weight: 600 !important;
    font-size: 16px !important;
    color: #2c3e50 !important;
}

[data-testid="metric-container"] > div:nth-child(2) {
    font-size: 32px !important;
    font-weight: 800 !important;
    color: #0099b5 !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1) !important;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0099b5 0%, #1e8e3e 100%) !important;
    border-right: 4px solid #ce1126 !important;
}

/* Data tables */
.dataframe {
    border: 2px solid #0099b5 !important;
    border-radius: 10px !important;
    overflow: hidden !important;
    background: white !important;
}

.dataframe thead th {
    background: linear-gradient(135deg, #0099b5 0%, #007a99 100%) !important;
    color: white !important;
    font-weight: 700 !important;
    padding: 15px !important;
    text-align: center !important;
}

/* Traditional pattern for dividers */
.stMarkdown hr {
    border: none !important;
    height: 4px !important;
    background: linear-gradient(90deg, 
        #0099b5 0%, #0099b5 25%, 
        #1e8e3e 25%, #1e8e3e 50%, 
        #ce1126 50%, #ce1126 75%, 
        #0099b5 75%, #0099b5 100%) !important;
    margin: 40px 0 !important;
    border-radius: 2px !important;
}
</style>
""", unsafe_allow_html=True)

# Your page content
st.title("📁 Upload Sales Data")

st.markdown("""
<div style="text-align: center; color: #666; margin-bottom: 30px;">
    <h3>🌿 Traditional Uzbek Analytics Platform 🌿</h3>
</div>
""", unsafe_allow_html=True)

uploaded = st.file_uploader("Upload your CSV file with sales data", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.session_state["raw_df"] = df
    st.success("File uploaded successfully!")
    
    st.subheader("📊 Data Preview")
    st.dataframe(df.head())
    
    # Show file info with metrics
    st.subheader("📈 File Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Rows", len(df))
    with col2:
        st.metric("Total Columns", len(df.columns))
    with col3:
        st.metric("File Size", f"{uploaded.size / 1024:.1f} KB")