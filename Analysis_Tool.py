import pandas as pd
import streamlit as st
import data_frame

def app():
    st.markdown("""<h1 style='text-align: center; font-family: Candara; font-size: 50px'>
                    ANALYSIS TOOL
                    </h1>""", unsafe_allow_html=True)
    all_data = pd.read_csv('car_data.csv')

    with st.container():
        st.write('---')
        st.info('Data Table')
        df = pd.DataFrame(all_data, columns=['Brand', 'Year of manufacture', 'Gia so'])
        #df.to_csv('car_data.csv')
        df = df.rename(columns={'Gia so': 'Price'})
        st.dataframe(df, use_container_width=True)

    with st.container():
        st.write('---')
        select = st.radio('Quantitative analysis', ['All', 'Brand', 'Years of manufacture'], horizontal=True)
        if select == 'Brand':
            st.info('Number of each brand')
            st.bar_chart(df['Brand'].value_counts())
        elif select == 'Years of manufacture':
            st.info('Number of years of manufacture')
            st.bar_chart(df['Year of manufacture'].value_counts())
        else:
            col1, col2 = st.columns(2)
            with col1:
                st.info('Number of each brand')
                st.bar_chart(df['Brand'].value_counts())
            with col2:
                st.info('Number of years of manufacture')
                st.bar_chart(df['Year of manufacture'].value_counts())

    with st.container():
        st.write('---')
        brand_set = list(set(df['Brand']))
        chart_analysis = []

        for i in range(len(brand_set)):
            new_data_frame = df[df['Brand'] == brand_set[i]]
            sumNum = new_data_frame.loc[:, 'Price'].sum()
            AvgPrice = sumNum / len(new_data_frame)
            chart_analysis.append([brand_set[i], AvgPrice])
        analistData = pd.DataFrame(chart_analysis, columns=['Brand', 'Averange Price'])

        st.info("Averange Price Of Each Brand")
        st.bar_chart(analistData, x='Brand', y='Averange Price')
    
    with st.container():
        st.write('---')
        new_tag_brand = st.sidebar.selectbox('Brand', sorted(list(set(all_data['Brand']))), key='new_brand_key')   
        if 'info' not in st.session_state:
            st.session_state['info'] = df
        if 'tag_brand' not in st.session_state:
            st.session_state['tag_brand'] = new_tag_brand

        st.session_state['info'] = df[df['Brand'] == st.session_state['tag_brand']]
        year_set = list(set(st.session_state['info']['Year of manufacture']))
        analysis = []
        for i in range(len(year_set)):
            new_data_frame = st.session_state['info'][st.session_state['info']['Year of manufacture'] == year_set[i]]
            sumNum = new_data_frame.loc[:, 'Gia so'].sum()
            AvgPrice = sumNum / len(new_data_frame)
            analysis.append([year_set[i], AvgPrice])
        analist = pd.DataFrame(analysis, columns=['Year of manufacture', 'Averange Price'])
        st.dataframe(new_data_frame)
        st.info("Averange Price Of Each Year")
        st.bar_chart(analist, x='Year of manufacture', y='Averange Price')

        
        


    

    
