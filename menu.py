import streamlit as st
from streamlit_option_menu import option_menu

import About_Us, Analysis_Tool, Search_Tool

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
                options=["About Us", "Search Tool", "Analysis Tool"],
                icons=['person-circle', "search", "database"],
                menu_icon='menu-button-wide-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-colour": "black"} ,
                    "icon": {"colour": "white", "font-size": "23px"},
                    "nav-link": {"colour": "white", "font-size": "20px", "margin":"0px", "--hover-color": "#9e7157"}, 
                    "nav-link-selected": {"background-color": "#E3651D"}
                    }
                    
            )
        if app == "Search Tool":
            Search_Tool.app()
        if app == "Analysis Tool":
            Analysis_Tool.app()
        if app == "About Us":
            About_Us.app()
    
    run()