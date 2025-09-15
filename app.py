import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="CORD-19 Explorer", layout="wide")

st.title("📊 CORD-19 Research Explorer")
st.markdown("Explore COVID-19 research abstracts and generate word clouds from titles.")

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("metadata.csv", low_memory=False)
    except FileNotFoundError:
        st.warning("No metadata.csv found. Please upload a CSV file.")
        df = pd.DataFrame()
    return df

df = load_data()

# File upload fallback
if df.empty:
    uploaded_file = st.file_uploader("Upload metadata.csv", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)

# Proceed only if data is available
if not df.empty:
    # Sidebar filters
    st.sidebar.header("🔍 Filter Options")
    keyword = st.sidebar.text_input("Search titles by keyword")

    if keyword:
        filtered_df = df[df['title'].str.contains(keyword, case=False, na=False)]
    else:
        filtered_df = df

    st.subheader(f"Showing {len(filtered_df)} results")
    st.dataframe(filtered_df[['title', 'abstract']].dropna().reset_index(drop=True))

    # Word cloud from titles
    if not filtered_df.empty:
        title_text = " ".join(filtered_df['title'].dropna())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(title_text)

        st.subheader("🧠 Title Word Cloud")
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)
else:
    st.stop()