import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import link_web
import scrap_data

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

url = link_web.link_truy_cap(tag_brand, tag_year, tag_price)


link_list = link_web.link_page(url)

if 'page_count' not in st.session_state:
    st.session_state['page_count'] = 0
if 'link_list' not in st.session_state:
    st.session_state['link_list'] = link_list

tab1, tab2 = st.tabs(['Car List', 'Analysis'])
#Lấy data của từng trang
with tab1:
    with st.form(key="Search Item"):
        nav1, nav2 = st.columns([2, 1])
        with nav1:
            search = st.text_input('Search Input', placeholder='Insert...')
        with nav2:
            st.text('Submit')
            submit_serach = st.form_submit_button("Search")
 
    scrap_data.crawl_data(link_list[st.session_state['page_count']])

    if submit_serach:
        st.session_state['link_list'] = link_web.link_search_item(url, search)
    
    
    st.sidebar.header('Page')
    col1, col2 = st.sidebar.columns(2)
    with col1:
        page_previous_1 = st.button('Previous')
        if page_previous_1:
            st.session_state.page_count -= 1
    with col2:
        page_next_1 = st.button('Next')
        if page_next_1:
            st.session_state.page_count += 1

    

    # with col3:
    #     page_input = st.number_input(f'{st.session_state.page_count}/{len(link_list)}', placeholder='Insert page number...')
    #     st.session_state.page_count = int(page_input)


    

with tab2:
    all_info = []

    for j in range(len(link_list)):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cars = soup.find_all("li", class_=["car-item row1", "car-item row2"] )

        for car in cars:
            model = car.find("div", class_="cb2_02").text
            
            split_name = model.replace('-', ' ').split()
            car_name = ' '.join(split_name[:-1])
            car_brand = car_name.split()[0]
            year_of_manufacture = split_name[-1]

            price = car.find("div", class_="cb3").text

            split_price = price.split()
            if 'Tỷ' in split_price:
                new_price = int(split_price[split_price.index('Tỷ') - 1]) * 1000 + int(split_price[split_price.index('Tỷ') + 1])
            elif 'Triệu' in split_price:
                new_price = int(split_price[split_price.index('Triệu') - 1]) 

            all_info.append([car_brand, car_name, year_of_manufacture, new_price])

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

