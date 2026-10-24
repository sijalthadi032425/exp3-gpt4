import streamlit as st

def get_user_input():
    st.header("1. User Input")
    customer_name = st.text_input("Customer Name", value="")
    email_subject = st.text_input("Email Subject", value="")
    customer_email = st.text_area("Customer Email", value="", height=100)
    
    if st.button("Submit Email"):
        if customer_name and email_subject and customer_email:
            st.session_state['input_data'] = {
                'Customer Name': customer_name,
                'Email Subject': email_subject,
                'Customer Email': customer_email
            }
            st.success("Input saved successfully!")
            return True
        else:
            st.warning("Please fill in all fields.")
    
    return False

def display_input():
    if 'input_data' in st.session_state:
        st.subheader("Entered Details")
        data = st.session_state['input_data']
        st.text(f"Customer Name : {data['Customer Name']}")
        st.text(f"Subject       : {data['Email Subject']}")
        st.text("Customer Email:")
        st.text(data['Customer Email'])
        return data
    return None
