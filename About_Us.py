import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title=" About Us",
                   layout="wide")



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
st.title("Welcome to Used Car Search and Analysis Tool")
st.balloons()

with st.container():
    st.write('---')
    st.title(":red[Meet Our Team]")
    st.subheader('Our Members')
    mem_1, mem_2, mem_3, mem_4 = st.columns(4)
    with mem_1:
        st.image("img/img/nmh.jpg", caption="Nguyen Minh Huong")
    
    with mem_2:
        st.image("img/img/4264.webp", caption="Luong Quynh Chi")

    with mem_3:
        st.image("img/img/4264.webp", caption="Nguyen Van Ngoc")

    with mem_4:
        st.image("img/img/ttq.jpg", caption="Tran Truc Quynh")



with st.container():
    st.write('---')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(' About The Project')
        st.write('This app will help you find your wanted car easily by navigating and filtering through a diverse range of used cars based on brand, year of manufacture, \
                 and price range.But it dont stop there,our tool could offering you a market trend analysis feature. Gain valuable insights into pricing trends, popular \
                 brands, and market dynamics to stay ahead of the curve. Welcome to a smarter way to find, evaluate, and analyze used cars.')
    with col2:
        lottie = load_lottiefile("img/img/intro_img.json")
        st_lottie(lottie, speed=1, reverse=False, loop=True, quality="low")


