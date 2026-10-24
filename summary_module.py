import streamlit as st
from utils import call_ollama

def generate_summary(customer_email):
    prompt = f"""
Summarize the customer's issue from the following email in exactly 50 words or less.

Email: "{customer_email}"

Summary:
"""
    return call_ollama(prompt, model="llama3.2")

def render_conversation_summary():
    st.header("6. Conversation Summary")
    if 'input_data' in st.session_state:
        if st.button("Generate Summary"):
            with st.spinner("Summarizing..."):
                current_email = st.session_state['input_data']['Customer Email']
                summary = generate_summary(current_email)
                st.session_state['conversation_summary'] = summary
                
        if 'conversation_summary' in st.session_state:
            st.subheader("Summary")
            st.write(st.session_state['conversation_summary'])
    else:
        st.info("Please submit an email first.")
