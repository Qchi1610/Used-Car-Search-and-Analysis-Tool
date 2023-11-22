import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Used Car Search and Analysis Tool')
st.sidebar.header('Search Bar')
tag_brand = st.sidebar.selectbox('Brand', ['All', 'Audi', 'Bentley', 'BMW', 'Chevrolet', 'Daewoo', 'Ford', 'Honda', 'Hyundai', 'Isuzu', 'Jeep', 'Kia', 'LandRover', 'Lexus', 'Mazda', 'Mercedes Benz', 'MG', 'Mini', 'Mitsubishi', 'Nissan', 'Peugeot', 'Porsche', 'Subaru', 'Suzuki', 'Toyota', 'VinFast', 'Volkswagen', 'Volvo', 'Other'])   
tag_year = st.sidebar.selectbox('Year Of Manufacture', ['All'] + list(reversed(range(1994, 2024))))
tag_price = st.sidebar.slider('Price Range', 0, 2000, (0, 2000))


sidebar_expanded = st.sidebar.button('Expand Condition [+]')
if sidebar_expanded:
    tag_fuel = st.sidebar.selectbox('Fuel', ['All', 'Gasoline', 'Diesel', 'Hybrid', 'Electricity', 'Other'])
    tag_origin = st.sidebar.selectbox('Origin', ['All', 'Imported Car', 'Domestically Assembled Car'])
    tag_color = st.sidebar.selectbox('Color', ['All', 'Silver', 'Light Yellow', 'Red', 'Bronze', 'Black', 'Gray', 'Pink', 'Cream', 'Other'])
    tag_styles = st.sidebar.selectbox('Styles', ['All', 'Sedan', 'Coupe', 'SUV/ Crossover', 'Hatchback', 'Other'])
    tag_seats = st.sidebar.selectbox('Seats', ['All', '1-3', '4-6', '7-8', '9-16', '> 16'])
    tag_drive = st.sidebar.selectbox('Drive', ['All', 'FWD - Front Wheel Drive', 'RWD - Rear Wheel Drive', '4-Wheel Drive'])
    tag_pic = st.sidebar.selectbox('Picture', ['All', 'With Picture', 'No Picture'])

url1 = 'https://bonbanh.com/oto'
url2 = '-cu-da-qua-su-dung'
if tag_brand == 'All' and tag_year == 'All' and tag_price[0] == 0 and tag_price[1] == 2000:
    url1 = 'https://bonbanh.com/oto-cu-da-qua-su-dung'
else:
    if tag_brand == 'Other':
        url1 = 'https://bonbanh.com/oto/hang_khac'
    elif tag_brand != 'All':
        url1 = f'https://bonbanh.com/oto/{tag_brand}'

    if tag_year != 'All':
        url1 = url1 + f'-nam-{tag_year}'

url = url1 + url2

if tag_price[0] != 0 and tag_price[1] != 2000:
    url = url + f'-gia-tu-{tag_price[0]}-{tag_price[1]}-trieu'
elif tag_price[0] != 0:
    url = url + f'-gia-tren-{tag_price[0]}-trieu'
elif tag_price[1] != 2000:
    url = url + f'-gia-duoi-{tag_price[1]}-trieu'
st.write(url)

tab1, tab2 = st.tabs(['Car List', 'Analysis'])

link_list = []
link_list.append(url)
all_info = []

#Link truy cập vào từng trang của website
for i in range(2, 11):
    new_link = url + f'/page,{i}'
    link_list.append(new_link)

#Lấy data của từng trang
with tab1:
    for j in range(len(link_list)):
        response = requests.get(link_list[j])
        soup = BeautifulSoup(response.text, 'html.parser')
        cars = soup.find_all("li", class_=["car-item row1", "car-item row2"] )

        for car in cars:
            with st.container():
                st.write("---")
                model = car.find("div", class_="cb2_02").text

                split_name = model.replace('-', ' ').split()
                car_name = ' '.join(split_name[:-1])
                car_brand = car_name.split()[0]
                year_of_manufacture = split_name[-1]

                st.info(model)

                left_column, right_column = st.columns(2)
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
                        st.image(car_img)
            all_info.append([car_brand, car_name, year_of_manufacture, new_price])
        break

with tab2:
    df = pd.DataFrame(all_info, columns=['Brand', 'Name', 'Year of manufacture', 'Price'])
    #df.to_csv('car_data.csv')

    st.dataframe(df)
    st.bar_chart(df['Brand'].value_counts())
    st.bar_chart(df['Year of manufacture'].value_counts())

    brand_set = list(set(df['Brand']))
    chart_analysis = []

    for i in range(len(brand_set)):
        d = df[df['Brand'] == brand_set[i]]
        #d.to_csv()
        listPrice = list(d['Price'])
        sumNum = 0
        AvgPrice = 0
        for j in range(len(listPrice)):
            sumNum += listPrice[j] 
        AvgPrice = sumNum / len(listPrice)
        chart_analysis.append([brand_set[i], AvgPrice])
    analistData = pd.DataFrame(chart_analysis, columns=['Brand', 'Averange Price'])
    st.bar_chart(analistData, x='Brand', y='Averange Price')





    