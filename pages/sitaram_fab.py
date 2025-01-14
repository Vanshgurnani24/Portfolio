import streamlit as st

import pathlib
def load_css(file_path):
   with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path=pathlib.Path("assets/style.css")
load_css(css_path)

col1,col2,col3=st.columns(3,gap='large')
col2.markdown(""" 
<div class="card">
  <div class="card-details">
    <p class="text-title">Sitaram Fabrics</p>
    <p class="text-body">Grey fabric producer</p>
  </div>
  <button class="card-button">Updates Coming Soon</button>
</div>""",unsafe_allow_html=True)