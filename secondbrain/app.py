# main.py
import os
import tempfile

import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import SupabaseVectorStore
from supabase import Client, create_client
from helpers.source_embedding import load_pdf, load_embedding_model, retriver, source_docs
from helpers.add_knowledge import AddKnowledge


# Set the theme
st.set_page_config(
    page_title="SecondBrain",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.title("SecondBrain 🧠")
st.markdown("Store your knowledge in a vector store and query it with OpenAI's GPT-3/4.")

st.markdown("---\n\n")

user_choice = st.sidebar.selectbox("Select Your Choice: ", options=['Add Knowledge', 'Chat with your Brain', 'Forget', "Explore"])


if user_choice == 'Add Knowledge':
    
    st.sidebar.title("Configuration")
    st.sidebar.markdown(
        "Choose your chunk size and overlap for adding knowledge.")
    chunk_size = st.sidebar.slider(label="Select Chunk Size", min_value=100, max_value=1000, step=1, value=500)
    chunk_overlap = st.sidebar.slider(label="Select Chunk Overlap", min_value=0, max_value=500, step=1, value=10)
    
    knowledge_sources = st.file_uploader(label="Upload Multiple PDFs: ", accept_multiple_files=True)
    if st.button("Add To Database"):
        add_knowledge = AddKnowledge()
        files = add_knowledge.extract_content(knowledge_sources, chunk_size, chunk_overlap)
        for f in files:
            st.text(f)


if user_choice == "Source Embedding":

    pass