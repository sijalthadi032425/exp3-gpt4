import streamlit as st
from utils import call_ollama

def improve_tone(reply, tone):
    prompt = f"""
Rewrite the following email reply to sound more {tone}. 
Keep the core message the same.

Original Reply:
"{reply}"

Rewritten Reply ({tone} tone):
"""
    return call_ollama(prompt, model="llama3.2")

def render_tone_improver():
    st.header("5. Tone Improver")
    if 'generated_reply' in st.session_state:
        selected_tone = st.selectbox("Select Tone", ["Friendly", "Formal", "Empathetic"])
        
        if st.button("Rewrite Reply"):
            with st.spinner(f"Rewriting in {selected_tone} tone..."):
                current_reply = st.session_state['generated_reply']
                new_reply = improve_tone(current_reply, selected_tone.lower())
                st.session_state['generated_reply'] = new_reply
                st.success("Reply updated!")
                st.write(new_reply)
    else:
        st.info("Please generate a reply first.")
