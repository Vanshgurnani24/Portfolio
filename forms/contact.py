import re
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

conn=st.connection(name='gsheets',type=GSheetsConnection)
existing_data=conn.read(worksheet='Personal_contact',usecols=list(range(5)),ttl=5)

existing_data=existing_data.dropna(how='all')
def is_valid_email(email):
    email_pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern,email) is not None


def contact_form():
    with st.form("contact_form"):
        name=st.text_input("First Name")
        email=st.text_input("Email Address")
        phonenumber=st.text_input("Phone number")
        message=st.text_area("Your Message")
        submit_button=st.form_submit_button("Submit")

        if submit_button:
            if not name:
                st.error("Please provide your name",icon="👨")
                st.stop()

            if not email:
                st.error("Please provide your email address",icon="✉")
                st.stop()
            
            if not is_valid_email(email):
                st.error("Please provide a valid email address",icon="📧")
                st.stop()
            if not message:
                st.error("Please provide a message",icon="💭")
                st.stop()

            user_data=pd.DataFrame(
        [
        {
          "Name":name,
          "Email":email,
          "Mobile":phonenumber,
          "Message":message,
          "Date":pd.Timestamp.now()
        }
        ]
      )
            updated_df=pd.concat([existing_data,user_data],ignore_index=True)
            conn.update(worksheet="Personal_contact",data=updated_df)
            st.success("Message sent successfully!")