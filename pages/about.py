import streamlit as st
from forms.contact import contact_form
import pathlib

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path=pathlib.Path("assets/style.css")
load_css(css_path)



col1,col2=st.columns(2,gap="small",vertical_alignment='center')


@st.dialog(title="Contact Me",width="small")
def show_contact_form():
    contact_form()


with col1:
    st.image("./assets/me.png",width=230)
with col2:
    st.title("Vansh Gurnani",anchor=False)
    st.write(
        "A computer engineering student passionate about data science, building a network of astute minds to cultivate teamwork and growth."
    )
    if st.button("✉ Contact me",key='contact-me-button'):
        show_contact_form()

# Qualifications and expiriences

st.write("\n")
st.subheader("Experience And Qualifications",anchor=False,divider='red')
st.write(
    """
        -  Nearly a year of experience in designing and developing robust CRUD applications.
        - Strong hands on experience and knowledge in Python, Excel and SQL.
        - Good understanding of CRUD applications.
        - A collaborative team player and leader, efficiently managing tasks to deliver high-quality results.
    """
)


# Skills
#Hard Skills
st.write("\n")
st.subheader("Hard Skills",anchor=False,divider='green')
st.write(
    """
    - Technologies: Frontend Developer, Backend Developer, CRUD Developer.
    - Programming: Python, SQL, HTML, CSS,C,C++.
    - Frameworks: Pandas, Numpy, Matplotlib, Seaborn, Scikit, Streamlit, Flask.
    - Data Visualization: MS Excel, PowerBi, Plotly. 
    - Video Editing: Adobe Premiere pro, Adobe After Effects, Wondershare Filmora, Sony Vegas Pro, DaVinci Resolve.
    - Photo Editing: Adobe Photoshop, Adobe Lightroom, Canva.
    - Vector Base Editing: Adobe Illustrator.
    - Databases: MySQL.
    """
)

#Soft Skills
st.write("\n")
st.subheader("Soft Skills",anchor=False,divider='blue')
st.write(
    """
    - Leadership
    - Creativity
    - Communications
    - Public Speaking
    - Time Management
    - Problem Solving
    """
)




st.markdown("---")
st.html("<H1 style='text-align: center;'>Feel free to reach out!</H1>")
col1,col2=st.columns(2,gap='large',vertical_alignment='bottom')
col1.link_button("INSTAGRAM",url="https://www.instagram.com/vansh_gurnani24",use_container_width=True,type='primary')
col2.link_button("LINKEDIN",url="https://www.linkedin.com/in/vansh-gurnani-a85279346/",use_container_width=True,type='primary')
