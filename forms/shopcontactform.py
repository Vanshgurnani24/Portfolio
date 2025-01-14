import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import re


conn=st.connection(name='gsheets',type=GSheetsConnection)
existing_data=conn.read(worksheet='Shop_Contact',usecols=list(range(5)),ttl=5)

existing_data=existing_data.dropna(how='all')

def is_valid_email(email):
  email_pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
  return re.match(email_pattern,email) is not None

def shop_contact_form():
  with st.form("Query-form",clear_on_submit=True):
    name=st.text_input("Your Name",placeholder="Your Name")
    c1,c2=st.columns(2,gap='medium')
    email=c1.text_input("Email Address",placeholder="Email Address")
    PhoneNumber=c2.text_input("Phone Number",placeholder="Phone Number")
    message=st.text_area("Drop a Message",placeholder="Your Message Here")
    if st.form_submit_button("Send Message",type='secondary',use_container_width=True):
      if not name:
        st.error("Please enter your name",icon="❌")
        st.stop()
      
      if not PhoneNumber or not(PhoneNumber.isdigit()) or len(PhoneNumber)!=10:
        st.error("Please enter a valid phone number",icon="📞")
        st.stop()
      
      if not email or not is_valid_email(email):
        st.error("Please enter a valid email address",icon="📧")
        st.stop()
      
      if not message:
        st.error("Please enter a message",icon="💭")
        st.stop()
      
      user_data=pd.DataFrame(
        [
        {
          "Name":name,
          "Email":email,
          "PhoneNumber":PhoneNumber,
          "Message":message,
          "Date":pd.Timestamp.now()
        }
        ]
      )
      updated_df=pd.concat([existing_data,user_data],ignore_index=True)
      conn.update(worksheet="Shop_Contact",data=updated_df)
      st.success("Message sent successfully!")