import pandas as pd

def data_table(tag_brand, tag_year, tag_price, all_data): 
    if tag_brand == 'All' and tag_year == 'All' and tag_price[0] == 0 and tag_price[1] == 2000:
        data = all_data
    else:
        if tag_brand == 'Other':
            list_brand = ['Audi', 'Bentley', 'BMW', 'Chevrolet', 'Daewoo', 'Ford', 'Honda', 'Hyundai', 'Isuzu', 'Jeep', 'Kia', 'LandRover', 'Lexus', 'Mazda', 'Mercedes', 'MG', 'Mini', 'Mitsubishi', 'Nissan', 'Peugeot', 'Porsche', 'Subaru', 
                        'Suzuki', 'Toyota', 'VinFast', 'Volkswagen', 'Volvo', 'Acura','Alfa','Asia','Aston','Baic','Brilliance','Buick','BYD','Cadillac','Changan','Chery','Chrysler','Citroen','Daihatsu',
                        'Datsun','Dodge','Dongben','Dongfeng','Ferrari','Fiat','Gaz','Geely','Genesis','GMC','Haima','Haval','Hino','Hongqi','Hummer','Infiniti','Jaguar',
                        'JRD','Lada','Lamborghini','Lifan','Lincoln','Luxgen','Maserati','Maybach','McLaren','Mekong','Mercury','Morgan','Opel','Pontiac','Proton','RAM','Renault',
                        'Rolls','Rover','Samsung','Scion','Skoda','Smart','SYM','Tesla','Thaco','Tobe','Ssangyong','UAZ','Vinaxuki','Wuling','Zotye']
            data = all_data[~all_data['Brand'].isin(list_brand)]

        elif tag_brand == 'Aston Martin':
            data = all_data[all_data['Brand'] == 'Aston']

        elif tag_brand == 'Alfa Romeo':
            data = all_data[all_data['Brand'] == 'Alfa']

        elif tag_brand == 'Rolls Royce':
            data = all_data[all_data['Brand'] == 'Rolls']

        elif tag_brand != 'All':
            data = all_data[all_data['Brand'] == tag_brand]

        if tag_year != 'All':
            data = data[data['Year of manufacture'] == str(tag_year)]

    if tag_price[0] != 0 and tag_price[1] != 2000:
        data = data[(data['Gia so'] >= tag_price[0]) and (data['Gia so'] <= tag_price[1])]

    elif tag_price[0] != 0:
        data = data[data['Gia so'] >= tag_price[0]]

    elif tag_price[1] != 2000:
        data = data[data['Gia so'] <= tag_price[1]]

    return data

def search_tool(regex: str, df):
    textlikes = df.select_dtypes(include=[object])
    return df[textlikes.apply(lambda column: column.str.contains(regex, regex=False, case = False, na=False)).any(axis = 1)]
