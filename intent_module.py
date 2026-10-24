import streamlit as st
from utils import call_ollama

def detect_intent(email_text):
    prompt = f"""
Analyze the following customer email and detect the intent. 
Choose ONLY ONE from the following list:
- Delivery Issue
- Refund Request
- Product Complaint
- Technical Support
- Order Cancellation
- General Inquiry

Email: "{email_text}"

Return ONLY the intent name, nothing else.
"""
    intent = call_ollama(prompt, model="llama3.2")
    # Clean up output just in case
    valid_intents = ["Delivery Issue", "Refund Request", "Product Complaint", 
                     "Technical Support", "Order Cancellation", "General Inquiry"]
    
    detected = "Unknown"
    for v_intent in valid_intents:
        if v_intent.lower() in intent.lower():
            detected = v_intent
            break
            
    if detected == "Unknown":
        detected = intent.strip()
        
    return detected

def render_intent_detection():
    st.header("2. Intent Detection")
    if 'input_data' in st.session_state:
        email_text = st.session_state['input_data']['Customer Email']
        if st.button("Detect Intent"):
            with st.spinner("Detecting intent using Ollama..."):
                intent = detect_intent(email_text)
                st.session_state['detected_intent'] = intent
                
        if 'detected_intent' in st.session_state:
            st.success(f"Detected Intent: {st.session_state['detected_intent']}")
            return st.session_state['detected_intent']
    else:
        st.info("Please submit an email first.")
    return None
