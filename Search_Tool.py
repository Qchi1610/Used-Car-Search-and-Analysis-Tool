import pandas as pd
import streamlit as st
import data_frame

def app():
    st.markdown("""<h1 style='text-align: center; font-family: Candara; font-size: 50px'>
                    USED CAR SEARCH
                    </h1>""", unsafe_allow_html=True)
    st.write('---')

    st.sidebar.header('Search Bar')
    tag_brand = st.sidebar.selectbox('Brand', ['All'] + sorted(['Audi', 'Bentley', 'BMW', 'Chevrolet', 'Daewoo', 'Ford', 'Honda', 'Hyundai', 'Isuzu', 'Jeep', 'Kia', 'LandRover', 'Lexus', 'Mazda', 'Mercedes Benz', 'MG', 'Mini', 'Mitsubishi', 'Nissan', 'Peugeot', 'Porsche', 'Subaru', 'Suzuki', 
                                            'Toyota', 'VinFast', 'Volkswagen', 'Volvo', 'Acura','Alfa Romeo','Asia','Aston Martin','Baic','Brilliance','Buick','BYD','Cadillac','Changan','Chery','Chrysler','Citroen','Daihatsu',
                                            'Datsun','Dodge','Dongben','Dongfeng','Ferrari','Fiat','Gaz','Geely','Genesis','GMC','Haima','Haval','Hino','Hongqi','Hummer','Infiniti','Jaguar',
                                            'JRD','Lada','Lamborghini','Lifan','Lincoln','Luxgen','Maserati','Maybach','McLaren','Mekong','Mercury','Morgan','Opel','Pontiac','Proton','RAM','Renault',
                                            'Rolls Royce','Rover','Samsung','Scion','Skoda','Smart','SYM','Tesla','Thaco','Tobe','Ssangyong','UAZ','Vinaxuki','Wuling','Zotye']) + ['Other'], key='brand')   
    tag_year = st.sidebar.selectbox('Year Of Manufacture', ['All'] + list(reversed(range(1994, 2024))), key='year')
    tag_price = st.sidebar.slider('Price Range', 0, 2000, [0, 2000], key='price')

    all_data = pd.read_csv('car_data.csv')
    if 'info' not in st.session_state:
        st.session_state['info'] = all_data
    if 'tag_brand' not in st.session_state:
        st.session_state['tag_brand'] = tag_brand
    if 'tag_year' not in st.session_state:
        st.session_state['tag_year'] = tag_year
    if 'tag_price' not in st.session_state:
        st.session_state['tag_price'] = tag_price
    if 'page_count' not in st.session_state:
        st.session_state['page_count'] = 0
    if 'first' not in st.session_state:
        st.session_state['first'] = 0
    if 'last' not in st.session_state:
        st.session_state['last'] = 20
    if 'Search' not in st.session_state:
        st.session_state['Search'] = False
    
    if st.session_state['Search'] == False:
        st.session_state['info'] = data_frame.data_table(tag_brand, tag_year, tag_price, all_data)
    else:
        st.session_state['info'] = data_frame.search_tool(search, all_data)

    return_home = st.button(":house: Home Page", on_click=data_frame.reset)
    if return_home:
        st.session_state['page_count'] = 0
        st.session_state['first'] = 0
        st.session_state['last'] = 20

    #Search Input
    with st.form(key="Search Item", clear_on_submit=True):
        nav1, nav2 = st.columns([4,2])
        with nav1:
            search = st.text_input('Search Input', placeholder='Insert...')
        with nav2:
            st.text('Search')
            submit_serach = st.form_submit_button("Search", on_click= data_frame.reset)
            if submit_serach:
                st.session_state['info'] = data_frame.search_tool(search, all_data)
                st.session_state['first'] = 0
                st.session_state['last'] = 20
                st.session_state['page_count'] = 0
                st.session_state['Search'] = True

    
    if tag_brand != st.session_state['tag_brand'] or tag_year != st.session_state['tag_year'] or tag_price != st.session_state['tag_price']:
        st.session_state['Search'] = False
        st.session_state['tag_brand'] = tag_brand 
        st.session_state['tag_year'] = tag_year
        st.session_state['tag_price'] = tag_price
        st.session_state['page_count'] = 0
        st.session_state['first'] = 0
        st.session_state['last'] = 20
    if len(st.session_state['info']) < st.session_state['last'] and len(st.session_state['info']) < 20 :
        st.session_state['last'] = len(st.session_state['info'])
    elif len(st.session_state['info']) < st.session_state['last']:
        st.session_state['last'] = len(st.session_state['info'])
    else:
        st.session_state['last'] = st.session_state['first'] + 20

    #Page Control
    st.sidebar.header('Page Control')
    col1, col2, col3 = st.sidebar.columns((3,2.5,2.5))
    with col1:
        page_previous_1 = st.button('Previous')
        if page_previous_1:
            st.session_state['page_count'] -= 1
            st.session_state['first'] -= 20
            st.session_state['last'] -= 20
    with col2:
        page_next_1 = st.button('Next')
        if page_next_1:
            st.session_state['page_count'] += 1
            st.session_state['first'] += 20
            st.session_state['last'] += 20 
    with col3:
        page_num = len(st.session_state['info']) / 20
        if st.session_state['page_count'] > page_num or st.session_state['page_count'] < 0:
            st.session_state['first'] = 0
            st.session_state['last'] = 20
            st.session_state['page_count'] = 0
        page_input = st.number_input(f'{st.session_state.page_count}/{int(page_num)}', value=None, placeholder='Insert page number...')
        if page_input:
            st.session_state['first'] = int(page_input * 20)
            st.session_state['last'] = int(page_input * 20 + 20)

    #Hiển thị thông tin xe
    if st.session_state['info'].empty == True:
        st.warning('No Result')
    else:
        with st.container():
            for i in range (st.session_state['first'], st.session_state['last']):
                st.write("---")
                st.info(st.session_state['info']['Model'].iloc[i])
                st.markdown(f"<a href=https://bonbanh.com/{st.session_state['info']['Link xe'].iloc[i]}> Click to get more detail  </a>", unsafe_allow_html=True)

                left_column, right_column = st.columns(2)
                with right_column:
                    tab_1, tab_2 = st.tabs(["Detail", "Desciption"])
                    with tab_1:
                        st.write("Năm sản xuất", st.session_state['info']['Year of manufacture'].iloc[i])
                        st.write("Giá: ", st.session_state['info']['Gia chu'].iloc[i])
                        st.write("Liên hệ:", st.session_state['info']['Lien he'].iloc[i])
                        st.write("Địa chỉ: ", st.session_state['info']['Dia chi'].iloc[i]) 
                        st.write(st.session_state['info']['SDT'].iloc[i])
                    with tab_2:
                        st.write("Thông số kĩ thuật: ", st.session_state['info']['Ki thuat'].iloc[i])
                        st.write("Thông tin mô tả: ", st.session_state['info']['Mo ta'].iloc[i])
                with left_column:
                    if st.session_state['info']['img'].iloc[i] == 'No Picture':
                        st.warning('No Picture')
                    else:
                        st.image(st.session_state['info']['img'].iloc[i], width= 250)
