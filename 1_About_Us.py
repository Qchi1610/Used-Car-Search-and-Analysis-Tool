import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title="About Us")



# page_background_img = """<style>
# [class="st-emotion-cache-1wmy9hl e1f1d6gn0"]{
# background-color: green'
#  opacity = 0.3;
# }<\style>"""



def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
# def load_lottieurl(url: str):
#     res = requests.get(url)
#     if res.status_code != 200:
#         return None
#     return res.json()


# st.markdown(page_background_img, unsafe_allow_html=True)

# new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
# st.markdown(new_title, unsafe_allow_html=True)

with st.container():
    st.write('---')
    st.title(":red[Meet Our Team]")
    st.subheader('Our Member')
    
    

with st.container():
    st.write('---')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('About The Project')
        st.write('this project....')
    with col2:
        lottie = load_lottiefile("img/intro_img.json")
        st_lottie(lottie, speed=1, reverse=False, loop=True, quality="low")
