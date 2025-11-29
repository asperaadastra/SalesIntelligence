import streamlit as st
import pandas as pd

# TEMPORARY FIX - Add this right after imports
st.markdown("""
<style>
/* Force dropdown visibility and proper width */
.stSelectbox {
    width: 100% !important;
}

div[data-baseweb="select"] > div {
    width: 100% !important;
    min-width: 400px !important;
}

div[data-baseweb="popover"] {
    width: 100% !important;
    min-width: 400px !important;
    background: white !important;
}

div[data-baseweb="popover"] div {
    color: #2c3e50 !important;
    background: white !important;
    white-space: normal !important;
    padding: 12px !important;
}

div[data-baseweb="select"] > div > div > div {
    color: #2c3e50 !important;
}
</style>
""", unsafe_allow_html=True)

def load_css_file(file_path="styles/default.css"):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file()

# Rest of your page2.py code...
st.title("🔧 Column Mapping")

if "raw_df" not in st.session_state:
    st.warning("Upload a CSV first.")
    st.stop()

df = st.session_state["raw_df"]

st.markdown('<div class="mapping-page-pattern">', unsafe_allow_html=True)

columns = df.columns.tolist()

st.write("Match your CSV columns to app fields:")

# You can also add some debugging info
st.write(f"📋 Available columns: {', '.join(columns)}")

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    date_col = st.selectbox("Date column:", columns, key="date_col")
    item_col = st.selectbox("Item name column:", columns, key="item_col")
    qty_col = st.selectbox("Quantity column:", columns, key="qty_col")

with col2:
    price_col = st.selectbox("Unit price column:", columns, key="price_col")
    category_col = st.selectbox("Category column:", columns, key="category_col")
    stock_col = st.selectbox("Stock column (optional):", ["None"] + columns, key="stock_col")

if st.button("💾 Save Mapping"):
    st.session_state["mapping"] = {
        "date": date_col,
        "item": item_col,
        "qty": qty_col,
        "price": price_col,
        "cat": category_col,
        "stock": None if stock_col == "None" else stock_col
    }
    st.success("✅ Mapping saved! You can now view the dashboard.")