import streamlit as st

class MentalHealthManagement:
    def __init__(self):
        st.header(":red[About MHM :material/local_hospital:]",divider='red',anchor=False)
        col1,col2=st.columns(2,gap='medium',vertical_alignment='center')
        with col1:
            st.html("""<p class='mhm-descritpion'>
                    This project have system for monitoring and supporting the mental health of children. It involves tailored surveillance, specialized assessment tools, and a dynamic tracking platform. By amalgamating data from diverse sources and employing technology-driven solutions, the project aims to provide timely interventions and foster a supportive environment for children's mental well-being
                </p>""")
        with col2:
            st.subheader(":red[This project is still under development :material/construction:]",anchor=False)
    
    def keyfeatures(self):
        st.header(":grey[Key Features :material/key:]",anchor=False,divider='grey')
        st.write("""
        - :grey[Appointment Booking]
        - :grey[Therapists and Patients Registration]
        - :grey[Analysis of Patients]
        - :grey[Report generation of Analysis]
        """)
    def Benefits(self):
        st.header(":green[Benefits :material/loyalty:]",divider='green',anchor=False)
        st.write("""
        - :green[Better communication]
        - :green[Reduced stigma]
        - :green[Enhanced patient care]
        - :green[Care coordination]
        - :green[Improved emergency response]
        - :green[Streamlined workflows]
        - :green[Transparency]
        """)
    def ProjectMedia(self):
        st.header(":violet[Project Media :material/tactic:]",anchor=False,divider='violet')
        with st.expander("Project Media :material/play_arrow:"):
            st.video("assets/videos/MHM video.mp4",autoplay=True,muted=True,loop=True)
            st.write("""
                - :violet[Note: This project is still under development and has not yet been deployed to GitHub. Once completed, it will be available for download and use on GitHub.]
            """)
    def TeamMembers(self):
        st.header(":orange[Project Team Members :material/groups:]",anchor=False,divider='orange')
        col1,col2=st.columns(2,gap='large',vertical_alignment='center')
        with col1:
            st.title("MAHARSHI BAROT",anchor=False)
            st.html("""
            A computer engineering student with a keen interest in both the fields of <strong>Cybersecurity</strong> and <strong>Website Development</strong>.
               My focus is to create visually appealing and user-friendly websites whilst also ensuring that strong security measures are maintained.
               The goal is to merge creativity with technical expertise that ensures a secure and attractive digital experience.
            """)
        with col2:
            st.image(image="assets/MaharshiBarot.jpg",use_container_width=True)
        
        st.subheader(":blue[Technology Proficiency]",divider='blue',anchor=False)
        st.write("""
        - :blue[Programming Skills: C, C++, HTML, CSS, JavaScript]
        - :blue[Frameworks: Bootstrap]
        - :blue[Databases: MySQL, MongoDB]
        - :blue[Networkig Skills: OSINT, nmap-scanning, wireshark, aircrack, JohnTheRipper, netcat, pen-testing.]
        """)

        st.subheader(":blue[Educational Qualification]",divider='blue',anchor=False)
        st.write("""
        - :blue[10th: GSEB(70%)[2020]]
        - :blue[12th GSEB Science(52%)[2022]]
        - :blue[Bachelors in Computer Engineering (2023-2026): 7.0CGPA]
        """)
        
        st.link_button("CONNECT WITH MAHARSHI",url="https://maharshibarot.streamlit.app/",type='primary',use_container_width=True)

    def projectLink(self):
        st.divider()
        if st.button("LINK TO THE PROJECT",use_container_width=True,key='meesho-outlet-button'):
            st.info("This project will be uploaded on github upon completion. Please check again later")
    



MHM=MentalHealthManagement()
MHM.keyfeatures()
MHM.Benefits()
MHM.ProjectMedia()
MHM.TeamMembers()
MHM.projectLink()