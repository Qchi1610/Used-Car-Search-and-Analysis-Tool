import requests
from bs4 import BeautifulSoup
import streamlit as st

def crawl_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cars = soup.find_all("li", class_=["car-item row1", "car-item row2"] )

    for car in cars:
        with st.container():
            st.write("---")
            model = car.find("div", class_="cb2_02").text
            link_car = car.find('a')


            split_name = model.replace('-', ' ').split()
            car_name = ' '.join(split_name[:-1])
            car_brand = car_name.split()[0]
            year_of_manufacture = split_name[-1]

            st.info(model)
            st.markdown(f"<a href=https://bonbanh.com/{link_car['href']}> Click to get more detail  </a>", unsafe_allow_html=True)


            left_column, right_column = st.columns((1,2))
            with right_column:
                tab_1, tab_2 = st.tabs(["Detail", "Desciption"])
                with tab_1:
                    status = car.find("div", class_="cb1")
                    car_status = status.contents[0]
                    price = car.find("div", class_="cb3").text

                    split_price = price.split()
                    if 'Tỷ' in split_price:
                        new_price = int(split_price[split_price.index('Tỷ') - 1]) * 1000 + int(split_price[split_price.index('Tỷ') + 1])
                    elif 'Triệu' in split_price:
                        new_price = int(split_price[split_price.index('Triệu') - 1])

                    descript = car.find("div", class_="cb6_02")
                    specifications = descript.contents[0]
                    descriptive = descript.find("p").get_text()

                    contact = car.find("div", class_="cb7")
                    trader = contact.contents[1].text.strip()
                    location = contact.contents[3].text.strip()
                    phone_number = contact.contents[-1].strip()

                    st.write(f"{car_status} ({year_of_manufacture})")
                    st.write("Giá: ", price)
                    st.write("Liên hệ:", trader)
                    st.write("Địa chỉ: ", location) 
                    st.write(phone_number)
                with tab_2:
                    st.write("Thông số kĩ thuật: ", specifications)
                    st.write("Thông tin mô tả: ", descriptive)
            with left_column:
                car_img = car.find('div', class_="cb5")
                car_img = car.find('img')
                car_img = car_img.get('src') 
                if 'https' not in car_img:
                    st.write('No Picture')
                else:
                    st.image(car_img, use_column_width="always")      
