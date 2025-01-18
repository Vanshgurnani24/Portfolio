import streamlit as st
import pathlib
import time as t

def load_css(file_path):
   with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path=pathlib.Path("assets/style.css")
load_css(css_path)

hide_st_style="""
    <style>
    #MainMenu{
    visibility:hidden;
    }
    footer {
        visibility:hidden;
    }
    </style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)






with st.container(key='loader-container'):
    loader_html = '<span class="loader"></span>'
    loader = st.markdown(loader_html, unsafe_allow_html=True)
    t.sleep(0.5) 
    loader.empty()

about_page=st.Page(
    page="pages/about.py",
    title="About me",
    icon=":material/account_circle:",
    default=True,   
)

my_shop_page=st.Page(
    page="pages/business.py",
    title="Shivam Emporium",
    icon=":material/apparel:",
)
sitaram_fab_page=st.Page(
    page="pages/sitaram_fab.py",
    title="Sitaram Fabrics",
    icon=":material/palette:",
)


chatbot_project=st.Page(
    page="pages/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
vendor_management_project=st.Page(
    page="pages/vendor_management.py",
    title="Vendor Management",
    icon=":material/storefront:",
)
loan_calculator=st.Page(
    page="pages/Loan_calculator.py",
    title="Loan Calculator",
    icon=":material/account_balance:",
)



# Setting up the 
# pg=st.navigation(pages=[about_page,my_shop_page,my_projects])


pg=st.navigation(
    {
        "Info":[about_page],
        "Projects":[chatbot_project,vendor_management_project,loan_calculator],
        "Businesses":[my_shop_page,sitaram_fab_page],
    }
)


# Shared on ALL PAGES
st.sidebar.text("Programmed with ♥ by Vansh")
pg.run()

