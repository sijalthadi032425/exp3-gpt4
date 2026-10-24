import streamlit as st
from utils import call_ollama

def generate_reply(customer_email, previous_reply):
    prompt = f"""
You are a professional customer support agent. 
Draft a reply to the customer's new email, using the previous reply as a reference for company policy and style.

Customer Email: "{customer_email}"
Previous Similar Reply: "{previous_reply}"

Write a professional email reply. Do not include subject lines, just the body.
"""
    return call_ollama(prompt, model="llama3.2")

def render_reply_generation():
    st.header("4. AI Reply Generation")
    if 'input_data' in st.session_state and 'similar_reply' in st.session_state:
        if st.button("Generate AI Reply"):
            with st.spinner("Generating professional reply..."):
                current_email = st.session_state['input_data']['Customer Email']
                prev_reply = st.session_state['similar_reply']
                reply = generate_reply(current_email, prev_reply)
                st.session_state['generated_reply'] = reply
                
        if 'generated_reply' in st.session_state:
            st.subheader("Generated Reply")
            st.write(st.session_state['generated_reply'])
            return st.session_state['generated_reply']
    else:
        st.info("Please complete input and similar email retrieval first.")
    return None
