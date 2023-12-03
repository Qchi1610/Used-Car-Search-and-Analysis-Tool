import streamlit as st
from streamlit_option_menu import option_menu

import Home, About_Us

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "funciton": function
        })

    def run():

        with st.sidebar:
            app = option_menu(
                menu_title="Menu",
                options=["Home", "About Us"],
                icons=['house-fill', 'person-circle'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-colour": "black"} ,"icon": {"colour": "white", "font-size": "23px"},
                                  "nav-link": {"colour": "white", "font-size": "20px"}, "nav-link-selected": {"background-color": "#02ab21"} }
                    
            )
            
        if app== "Home":
            Home.app()
        if app== "About Us":
            About_Us.app()
    
    run()
            
    
