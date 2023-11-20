import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image

st.title("User car search and Analysis Tool")

car = st.selectbox("Insert brand", ["Audi", "Bentley", "BMW", "Chevrolet","Daewoo","Ford","Honda","Hyundai",
                              "Isuzu","Jeep","Kia", "Landrover","Lexus","Mazda","Mercedes_Benz","MG","Mini","Mitsubishi",
                              "Nissan","Peugeot","Porsche","Subaru","Suzuki","Toyota","Vinfast","Volkswagen","Volvo"])

url = f"https://bonbanh.com/oto/{car}/"

res = requests.get(url)

soup = BeautifulSoup(res.content, "html.parser")

cars = soup.find_all("li", class_=["car-item row1", "car-item row2"] )

def get_img(car):
    car_img = car.find('div', class_="cb5")
    car_img = car.find('img')
    car_img = car_img.get('src')
    return car_img

for car in cars:
    with st.container():

        st.write("---")
        # tên xe
        model = car.find("div", class_="cb2_02").text
        st.info(model)

        
        #lấy thông tin xe
        status = car.find("div", class_="cb1")
        car_status = status.contents[0]
        year = status.find("b").get_text()
        
        #lấy giá xe
        price = car.find("div", class_="cb3").text

        #lấy thông số và thônng tin mô tả
        descript = car.find("div", class_="cb6_02")
        specifications = descript.contents[0]
        descriptive = descript.find("p").get_text()

        # lấy thông tin liên lạc
        contact = car.find("div", class_="cb7")
        trader = contact.contents[1].text.strip()
        location = contact.contents[3].text.strip()
        phone_number = contact.contents[-1].strip()

        #định dạng column
        left_column, right_column = st.columns(2)
        with right_column:
            tab_1, tab_2 = st.tabs(["Detail", "Desciption"])
            with tab_1:
                st.write(f"{car_status} ({year})")
                st.write("Giá: ", price)
                st.write("Liên hệ:", trader)
                st.write("Địa chỉ: ", location)  
                st.write(phone_number)  
            with tab_2:
                st.write("Thông số kĩ thuật: ", specifications)
                st.write("Thông tin mô tả: ", descriptive)
                
        with left_column:
            car_img = get_img(car) 
            st.image(car_img)