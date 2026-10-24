import streamlit as st
import os
from datetime import datetime

from input_module import get_user_input, display_input
from intent_module import render_intent_detection
from retrieval_module import render_retrieval_module
from reply_module import render_reply_generation
from tone_module import render_tone_improver
from summary_module import render_conversation_summary

def save_reply():
    st.header("7. Save Reply")
    if 'input_data' in st.session_state and 'generated_reply' in st.session_state and 'detected_intent' in st.session_state:
        if st.button("Save Conversation"):
            customer_email = st.session_state['input_data']['Customer Email']
            generated_reply = st.session_state['generated_reply']
            intent = st.session_state['detected_intent']
            date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            output_dir = os.path.join(os.path.dirname(__file__), 'outputs')
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, 'generated_reply.txt')
            
            content = f"Date: {date_str}\n"
            content += f"Intent: {intent}\n"
            content += f"Customer Email:\n{customer_email}\n\n"
            content += f"Generated Reply:\n{generated_reply}\n"
            content += "-" * 40 + "\n"
            
            with open(output_file, 'a') as f:
                f.write(content)
                
            st.success(f"Conversation saved to {output_file}")
    else:
        st.info("Please complete all previous steps to save.")


def main():
    st.title("Intelligent Email Assistant")
    
    # Render all modules
    get_user_input()
    display_input()
    
    st.markdown("---")
    render_intent_detection()
    
    st.markdown("---")
    render_retrieval_module()
    
    st.markdown("---")
    render_reply_generation()
    
    st.markdown("---")
    render_tone_improver()
    
    st.markdown("---")
    render_conversation_summary()
    
    st.markdown("---")
    save_reply()

if __name__ == "__main__":
    main()
