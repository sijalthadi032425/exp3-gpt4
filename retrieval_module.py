import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def load_data():
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'emails.csv')
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"Error loading CSV data: {e}")
        return None

def retrieve_similar_email(current_email):
    model = load_model()
    df = load_data()
    
    if df is None or df.empty:
        return None, None
        
    # Get embeddings for historical emails
    historical_emails = df['Customer_Email'].tolist()
    historical_embeddings = model.encode(historical_emails)
    
    # Get embedding for current email
    current_embedding = model.encode([current_email])
    
    # Calculate similarities
    similarities = cosine_similarity(current_embedding, historical_embeddings)[0]
    
    # Find the index of the most similar email
    most_similar_idx = similarities.argmax()
    
    previous_email = df.iloc[most_similar_idx]['Customer_Email']
    previous_reply = df.iloc[most_similar_idx]['Previous_Reply']
    
    return previous_email, previous_reply

def render_retrieval_module():
    st.header("3. Similar Email Retrieval")
    if 'input_data' in st.session_state:
        if st.button("Find Similar Email"):
            with st.spinner("Searching historical records..."):
                current_email = st.session_state['input_data']['Customer Email']
                prev_email, prev_reply = retrieve_similar_email(current_email)
                
                if prev_email and prev_reply:
                    st.session_state['similar_email'] = prev_email
                    st.session_state['similar_reply'] = prev_reply
                    
        if 'similar_email' in st.session_state:
            st.subheader("Most Similar Past Email")
            st.text(st.session_state['similar_email'])
            st.subheader("Previous Reply")
            st.text(st.session_state['similar_reply'])
            return st.session_state['similar_reply']
    else:
        st.info("Please submit an email first.")
    return None
