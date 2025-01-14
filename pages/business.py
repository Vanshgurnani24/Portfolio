import streamlit as st
import pandas as pd
import pathlib
from forms.shopcontactform import shop_contact_form

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path=pathlib.Path("assets/style.css")
load_css(css_path)

shop_location={
    'Latitude':21.197895686349593,
    'Longitude': 72.82403578086426
}

data=pd.DataFrame({
    'latitude': [shop_location['Latitude']],
    'longitude': [shop_location['Longitude']]
})


@st.dialog("Your Inquiry")
def show_contact_form():
    shop_contact_form()
    


st.markdown("<H1 style='text-align:center;'>SIDE BUSINESS</H1>",unsafe_allow_html=True)
st.markdown("---")
col1,col2=st.columns(2,gap='small',vertical_alignment='center')
with col1:
    st.image("./assets/shivam.png",width=230)
with col2:
    st.title("SHIVAM EMPORIUM",anchor=False)
    st.write("""Shivam Emporium offers high-quality ready-made men's garments, providing to various styles and preferences.
              Along with our retail counter, we also provide wholesale services based on customer demand.""")
    if st.button("Get in Touch",key='contact-me-button'):
        show_contact_form()
    
#Types of Products we sell
st.write("\n")
st.subheader("What We Offer",divider='red')
c1,c2=st.columns(2,gap='medium')
c1.write("""
    - Kurtas
    - Denim Jeans
    - Party Wear Jeans
    - Shirts (Full Sleeves)
    - T-Shirts (Full and Half Sleeves)
    - Woolen Attire
    """)
c2.write("""
        - Blazers
        - 5 peice tuxedo
        - 3 peice tuxedo
        - Rainwear
        - Socks & Hosiery
        - Denim Jackets
""")


# Our locations
st.write("\n")
st.subheader("Our Outlet",divider="green")
st.write("- Surat")
with st.expander("View Address",icon=':material/home:'):
    st.write("""Shivam Emporium, 10/2196, 
             opp. city Post Office, 
             Chauta Pul, 
             Nanavat, Surat, 
             Gujarat 395003
    """)
    st.map(data,color='#7FFFD4')

st.write("\n")
st.subheader("Online Outlets",divider='blue')
b1,b2=st.columns(2,gap='medium')
if b1.button("Meesho",key='meesho-outlet-button',use_container_width=True):
    st.info("The Launch of Our Online Outlet is Just Around the Corner.")
if b2.button("Amazon",key='amazon-outlet-button',use_container_width=True):
    st.info("The Launch of Our Online Outlet is Just Around the Corner.")