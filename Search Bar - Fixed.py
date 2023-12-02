import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

st.title('Used Car Search and Analysis Tool')
st.sidebar.header('Search Bar')
tag_brand = st.sidebar.selectbox('Brand', ['All', 'Audi', 'Bentley', 'BMW', 'Chevrolet', 'Daewoo', 'Ford', 'Honda',
                                           'Hyundai', 'Isuzu', 'Jeep', 'Kia', 'LandRover', 'Lexus', 'Mazda', 'Mercedes Benz',
                                           'MG', 'Mini', 'Mitsubishi', 'Nissan', 'Peugeot', 'Porsche', 'Subaru', 'Suzuki',
                                           'Toyota', 'VinFast', 'Volkswagen', 'Volvo', 'Other [+]'])     
tag_year = st.sidebar.selectbox('Year Of Manufacture', ['All'] + list(reversed(range(1994, 2024))))
tag_price = st.sidebar.slider('Price Range', 0, 2000, (0, 2000))


url1 = 'https://bonbanh.com/oto'
url2 = '-cu-da-qua-su-dung'

def display_radio_in_columns(data, num_columns):
    # Calculate the number of rows needed
    num_rows = (len(data) + num_columns - 1) // num_columns

    # Create the columns
    cols = st.columns(num_columns)

     # Iterate through the data and display radio buttons in columns
    for j in range(num_columns):
        col_data = data[j * num_rows:(j + 1) * num_rows]  # Get data for current column
        for choice in col_data:
            cols[j].radio("", choice)



if tag_brand == 'All' and tag_year == 'All' and tag_price[0] == 0 and tag_price[1] == 2000:
    url1 = 'https://bonbanh.com/oto-cu-da-qua-su-dung'
else:
        if tag_brand == 'Other [+]':
                other_brand = [['Acura'],['Alfa Romeo'],['Asia'],['Aston Martin'],['Baic'],['Brilliance'],['Buick'],['BYD'],['Cadillac'],['Changan'],['Chery'],['Chrysler'],['Citroen'],['Daihatsu'],
                                ['Datsun'],['Dodge'],['Dongben'],['Dongfeng'],['Ferrari'],['Fiat'],['Gaz'],['Geely'],['Genesis'],['GMC'],['Haima'],['Haval'],['Hino'],['Hongqi'],['Hummer'],['Infiniti'],['Jaguar'],
                                ['JRD'],['Lada'],['Lamborghini'],['Lifan'],['Lincoln'],['Luxgen'],['Maserati'],['Maybach'],['McLaren'],['Mekong'],['Mercury'],['Morgan'],['Opel'],[']Pontiac'],['Proton'],['RAM'],['Renault'],
                                ['Rolls Royce'],['Rover'],['Samsung'],['Scion'],['Skoda'],['Smart'],['SYM'],['Tesla'],['Thaco'],['Tobe'],['Ssangyong'],['UAZ'],['Vinaxuki'],['Wuling'],['Zotye'], ['Other']]
                
                num_columns = 5
                display_radio_in_columns(other_brand, num_columns)
                
                
                if other_brand != 'Other':
                        url1 = f'https://bonbanh.com/oto/{other_brand}'
                else:
                        url1 = 'https://bonbanh.com/oto/hang_khac'
                
        elif tag_brand == 'Audi':
                button1 = st.sidebar.radio('Audi', ['Q5','Q7', 'A6', 'A4', 'A8', 'A5', 'Q8', 'Q2', 'A7', '100', '200',
                                                        '80', '90', 'A1', 'A2', 'A3', 'Cabriolet', 'Coupe', 'E-tron',
                                                        'E-tron GT','Q3','Quattro','R8','RS2','RS4', 'S5','S8','TT','V8','Other'])
                if button1 != 'Other':
                        url1 = f'https://bonbanh.com/oto/audi-{button1}'
                else:
                        url1 = f'https://bonbanh.com/oto/audi-khac'
                
        elif tag_brand == 'Bentley':
                button2 = st.sidebar.radio('Bentley', ['Flying Spur', 'Mulsanne', 'Bentayga', 'Continental', 'Arnage',
                                                'Azure', 'Brooklands', 'Turbo', 'Other'])
                                                
                if button2 != 'Other':
                        url1 = f'https://bonbanh.com/oto/bentley-{button2}'
                else:
                        url1 = f'https://bonbanh.com/oto/bentley-khac'

        elif tag_brand == 'BMW':
                button3 = st.sidebar.radio('BMW', ['3 Series', '5 Series', '7 Series', 'X3', 'X6', 'X5', '4 Series', 
                                                        'X7', 'Z4', '1 Series', '2 Series', '6 Series', '8 Series', 'Alpina',
                                                        'i3', 'i8', 'iX', 'iX3', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M8', 'X1',
                                                        'X2', 'X4', 'XM', 'Z3', 'Z8', 'Other'])               
                if button3 != 'Other':
                        url1 = f'https://bonbanh.com/oto/bmw-{button3}'
                else:
                        url1 = f'https://bonbanh.com/oto/bmw-khac'

        elif tag_brand == 'Chevrolet':
                button4 = st.sidebar.radio('Chevrolet', ['Spark', 'Cruze', 'Captiva', 'Colorado', 'Aveo', 'Trailblazer', 
                                                                'Vivant', 'Orlando', 'Camaro', 'Trax', 'Lacetti', 'Alero', 'Astro', 
                                                                'Avanlanche', 'Beretta', 'Caprice', 'Cavalier', 'Chevyvan' ,'Cobalt',
                                                                'Corsica', 'Corvette', 'Equinox', 'Explorer', 'Express', 'Impala',
                                                                'Ipanema', 'Kalos', 'Lumina', 'Malibu', 'Matiz', 'Nubira', 'Prizm',
                                                                'S 10', 'Silverado', 'Spectrum', 'SSR', 'Suburban', 'Tahoe', 'Tracker',
                                                                'Trans Sport', 'Venture', 'Other'])
                                                
                if button4 != 'Other':
                        url1 = f'https://bonbanh.com/oto/chevrolet-{button4}'
                else:
                        url1 = f'https://bonbanh.com/oto/chevrolet-khac'
                
        elif tag_brand == 'Daewoo':
                button5 = st.sidebar.radio('Daewoo', ['Lacetti', 'Matiz', 'Gentra', 'Lanos', 'Nubira', 'Magnus', 'GentraX',
                                                        'Damas', 'Aranos', 'Arcadia', 'Brougham', 'Chairman', 'Cielo', 'Espero',
                                                        'Evanda', 'Istana', 'Kalos', 'Korando', 'Labo', 'Leganza', 'Lublin',
                                                        'Musso', 'Nexia', 'Novus', 'Polonez', 'Prince', 'Racer', 'Rexton',
                                                        'Rezzo', 'Statesman', 'Super Saloon', 'Tacuma', 'Tico', 'Tosca', 'Winstorm', 'Other'])
                                                
                if button5 != 'Other':
                        url1 = f'https://bonbanh.com/oto/deawoo-{button5}'
                else:
                        url1 = f'https://bonbanh.com/oto/daewoo-khac'
                
        elif tag_brand == 'Ford':
                button6 = st.sidebar.radio('Ford', ['Ranger', 'Everest', 'Territory', 'EcoSport', 'Transit', 'Focus', 
                                                        'Fiesta', 'Escape', 'Explorer', 'Tourneo', 'Acononline', 'Aerostar', 
                                                        'Aspire', 'Bronco', 'Capri', 'Caravan', 'Cargo', 'Club wagon', 'Contour',
                                                        'Courier', 'Crown victoria', 'E450', 'Edge', 'Escort', 'EscurSeon',
                                                        'Expedition', 'Express', 'F150', 'F250', 'F350', 'F450', 'F700', 'Flex',
                                                        'Focus C Max', 'Fusion', 'Galaxie', 'Imax', 'Ka', 'Laser', 'Maverick',
                                                        'Mondeo', 'Mustang', 'Orion', 'Pinto', 'Probe', 'Puma', 'Sierra', 'Streetka',
                                                        'Taurus', 'Tempo', 'Windstar' ,'Other'])
                                                
                if button6 != 'Other':
                        url1 = f'https://bonbanh.com/oto/bentley-{button6}'
                else:
                        url1 = f'https://bonbanh.com/oto/bentley-khac'
                
        elif tag_brand == 'Honda':
                button7 = st.sidebar.radio('Honda', ['CRV', 'City', 'Civic', 'HRV', 'Brio', 'BR V', 'Accord', 'Jazz',
                                                        'Odyssey', 'Capa', 'Concerto', 'CR X', 'CR Z', 'Domani', 'Element',
                                                        'FIT', 'FR V', 'Insight', 'Inspire', 'Integra', 'Legend', 'Life',
                                                        'Mobilo', 'NSX', 'Passport', 'Pilot', 'Prelude', 'S2000', 'Saber',
                                                        'Shuttle', 'Stream', 'Today', 'Torneo', 'Vigor', 'Z', 'Other'])
                                                
                if button7 != 'Other':
                        url1 = f'https://bonbanh.com/oto/honda-{button7}'
                else:
                        url1 = f'https://bonbanh.com/oto/honda-khac'

        elif tag_brand == 'Hyundai':
                button8 = st.sidebar.radio('Hyundai', ['Custin','Palisade','i10','SantaFe','Accent','Tucson','Elantra', 
                                                        'Kona','Creta','Getz','Stargazer','Avante','Atos','Azera','Centennial','Click', 
                                                        'County','Coupe','Custo','Dynasty','eMighty','Eon','Equus','Excel','Galloper', 
                                                        'Genesis','Gold','Grace','Grand Starex','Grandeur','H 1','H 100','H350','HD','i20', 
                                                        'i30','i40','Innovation','Ioniq 5','Lantra','Lavita','Libero','Marcia', 
                                                        'Matrix','Maxcruz','Mighty','Pony','Porter','S coupe','Santa Cruz','Santamo','Solati', 
                                                        'Sonata','Starex','Terracan','Tiburon','Trajet','Tuscani','Universe','Universe Xpress Luxury', 
                                                        'Veloster','Veracruz','Verna','Xcent','XG', 'Other'])
                                                
                if button8 != 'Other':
                        url1 = f'https://bonbanh.com/oto/hyundai-{button8}'
                else:
                        url1 = f'https://bonbanh.com/oto/hyundai-khac'
                
        elif tag_brand == 'Isuzu':
                button9 = st.sidebar.radio('Isuzu', ['Dmax','MU-X','QKR','Hi lander','NQR','NPR','Amigo','Ascender','Aska', 
                                                        'AXiom','Campo','D Cargo','Faster','FVR','Gemini','Midi','MU','NLR','NMR', 
                                                        'Panther','Pick up','Rodeo','Trooper','Turkuaz','Vehi cross','Wi zard', 'Other'])
                                                
                if button9 != 'Other':
                        url1 = f'https://bonbanh.com/oto/isuzu-{button9}'
                else:
                        url1 = f'https://bonbanh.com/oto/isuzu-khac' 
                
        elif tag_brand == 'Jeep':
                button10 = st.sidebar.radio('Jeep', ['Wrangler','Gladiator','A2','Cherokee','Grand cherokee','Liberty','CJ',
                                                        'Compass','Grand Wagoneer', 'Other'])
                                                
                if button10 != 'Other':
                        url1 = f'https://bonbanh.com/oto/jeep-{button10}'
                else:
                        url1 = f'https://bonbanh.com/oto/jeep-khac'

        elif tag_brand == 'Kia':
                button11 = st.sidebar.radio('Kia', ['Morning','Cerato','Carnival','K3','Sorento','Seltos','Sedona','Rio', 
                                                        'Carens','Soluto','Sonet','Forte','Avella','Bongo','Cadenza','Clarus','Concord', 
                                                        'Credos','Elan','Enterprise','Frontier','Jeep','Joice','K2700','K3000S','K4','K5', 
                                                        'K7','Lotze','Magentis','Opirus','Optima','Picanto','Potentia','Pregio','Pride',
                                                        'Quoris','Ray','Retona','Roadster','Rondo','Sephia','Shuma','Soul','Spectra', 
                                                        'Sportage','Visto','X Trek', 'Other'])
                                                
                if button11 != 'Other':
                        url1 = f'https://bonbanh.com/oto/kia-{button11}'
                else:
                        url1 = f'https://bonbanh.com/oto/kia-khac'
                        
        elif tag_brand == 'LandRover':
                button12 = st.sidebar.radio('LandRover', ['Range Rover','Range Rover Evoque','Range Rover Sport', 
                                                                'Range Rover Velar','Defender','Discovery Sport','Discovery', 
                                                                'Freelander', 'Other'])
                                                
                if button12 != 'Other':
                        url1 = f'https://bonbanh.com/oto/landrover-{button12}'
                else:
                        url1 = f'https://bonbanh.com/oto/landrover-khac' 
                
        elif tag_brand == 'Lexus':
                button13 = st.sidebar.radio('Lexus', ['LX','RX','ES','GX','LS','NX','IS','GS','CT','HS','LC','LM','RC','SC','SL', 'Other'])
                                                
                if button13 != 'Other':
                        url1 = f'https://bonbanh.com/oto/lexus-{button13}'
                else:
                        url1 = f'https://bonbanh.com/oto/lexus-khac'   
                
        elif tag_brand == 'Mazda':
                button14 = st.sidebar.radio('Mazda', ['3','CX5','6','2','BT50','CX8','cx3','CX 30','323','626','121','323F',
                                                        '5','929','Atenza','AZ','B series','Bongo Friendee','Carol','Cronos','CX7', 
                                                        'CX9','Eunos','Familia','Millenia','MPV','MX 3','MX 5','MX 6','Pickup','Premacy', 
                                                        'RX 7','RX 8','Tribute','Xedos 9', 'Other'])
                                                
                if button14 != 'Other':
                        url1 = f'https://bonbanh.com/oto/mazda-{button14}'
                else:
                        url1 = f'https://bonbanh.com/oto/mazda-khac'   
                
        elif tag_brand == 'Mercedes Benz':
                button15 = st.sidebar.radio('Mercedes Benz', ['GLC','C class','E class','S class','Maybach','G class','GLS', 
                                                                'GLE Class','GLB','190','A class','AMG GT','Atego','B class', 
                                                                'CL class','CLA class','CLK class','CLS class','EQB','EQE','EQS', 
                                                                'GL','GLA class','GLK Class','M class','MB','ML Class','R class', 
                                                                'SL class','SLC','SLK class','SLR Mclaren','Sprinter','SR class', 
                                                                'V class','Vaneo','Viano','Vito', 'Other'])
                                                
                if button15 != 'Other':
                        url1 = f'https://bonbanh.com/oto/mercesdes_ben-{button15}'
                else:
                        url1 = f'https://bonbanh.com/oto/mercesdes_ben-khac'   

        elif tag_brand == 'MG':
                button16 = st.sidebar.radio('MG', ['5','ZS','HS','X','ZT','MGF','3','350C','6','Express','RX5', 'Other'])
                                                
                if button16 != 'Other':
                        url1 = f'https://bonbanh.com/oto/mg-{button16}'
                else:
                        url1 = f'https://bonbanh.com/oto/mg-khac'

        elif tag_brand == 'Mini':
                button17 = st.sidebar.radio('Mini', ['Cooper','One', 'Other'])
                                                
                if button17 != 'Other':
                        url1 = f'https://bonbanh.com/oto/mini-{button17}'
                else:
                        url1 = f'https://bonbanh.com/oto/mini-khac'

        elif tag_brand == 'Mitsubishi':
                button18 = st.sidebar.radio('Mitsubishi', ['Xpander','Triton','Attrage','Outlander','Pajero Sport','Pajero', 
                                                                'Jolie','Mirage','Grandis','Lancer','Zinger','Outlander Sport','3000GT', 
                                                                'Airtek','Canter','Carisma','Challenger','Chariot','Colt','Delica', 
                                                                'Diamante','Dion','Eclipse','EK wagon','FTO','Galant','Grunder','GTO', 
                                                                'Hover','IO','Jeep','L200','L300','L400','Libero','Minica','Montero', 
                                                                'Pinin','Santamo','Savrin','Sigma','Space Gear','Space wagon','Starion', 
                                                                'Veryca','Xforce', 'Other'])
                                                
                if button18 != 'Other':
                        url1 = f'https://bonbanh.com/oto/mitsubishi-{button18}'
                else:
                        url1 = f'https://bonbanh.com/oto/mitsubishi-khac'
                
        elif tag_brand == 'Nissan':
                button19 = st.sidebar.radio('Nissan', ['Navara','X trail','Almera','Sunny','Teana','Terra','Kicks','Grand livina', 
                                                        'Bluebird','Murano','Maxima','Qashqai','100NX','200SX','240SX','300ZX','350Z', 
                                                        '370Z','Altima','Armada','Avenir','Bassara','Cedric','Cefiro','Cima','Elgrand', 
                                                        'Frontier','Gloria','GT R','Juke','Langley','Largo','Laurel','Leaf','Liberty', 
                                                        'Livina','Micra','Moco','NV','Pathfinder','Patrol','Pick up','Pixo','Prairie', 
                                                        'Presage','Presea','President','Primastar','Primera','Pulsar','Quest','Rasheen', 
                                                        'Rogue','Safari','Sentra','Serena','Silvia','Skyline','Stagea','Stanza','Terrano', 
                                                        'Tiida','Tino','Urvan','Vanette','Versa','Wingroad','X Terra', 'Other'])
                                        
                if button19 != 'Other':
                        url1 = f'https://bonbanh.com/oto/nissan-{button19}'
                else:
                        url1 = f'https://bonbanh.com/oto/nissan-khac'
                
        elif tag_brand == 'Peugeot':
                button20 = st.sidebar.radio('Peugeot', ['3008','2008','5008','408','Traveller','208','107','205','206', 
                                                                '207','305','306','307','308','309','404','405','406','407','504', 
                                                                '505','508','605','607','807','Boxer','J5','RCZ', 'Other'])
                                                
                if button20 != 'Other':
                        url1 = f'https://bonbanh.com/oto/peugeot-{button20}'
                else:
                        url1 = f'https://bonbanh.com/oto/peugoet-khac'

        elif tag_brand == 'Porsche':
                button21 = st.sidebar.radio('Porsche', ['Cayenne','Panamera','Macan','718','911','Taycan','928','944', 
                                                                '968','Boxster','Carrera','Cayman', 'Other'])
                                                
                if button21 != 'Other':
                        url1 = f'https://bonbanh.com/oto/porsche-{button21}'
                else:
                        url1 = f'https://bonbanh.com/oto/porsche-khac'
                        
        elif tag_brand == 'Subaru':
                button22 = st.sidebar.radio('Subaru', ['Forester','Outback','BRZ','WRX','Tutto','Levorg','Dex','Impreza', 
                                                        'Legacy','Tribeca','XV', 'Other'])
                                                
                if button22 != 'Other':
                        url1 = f'https://bonbanh.com/oto/subaru-{button22}'
                else:
                        url1 = f'https://bonbanh.com/oto/subaru-khac'
                
        elif tag_brand == 'Suzuki':
                button23 = st.sidebar.radio('Suzuki', ['Swift','XL7','Super Carry Van','Ertiga','Super Carry Truck','Carry','Aerio', 
                                                        'Alto','APV','Baleno','Celerio','Ciaz','Cultis wagon','Esteem','Every landy', 
                                                        'Grand vitara','Jimmy','Kei','Liana','Samurai','SJ','SX4','Twin','Vitara','Wagon R+','X90', 'Other'])
                                                
                if button23 != 'Other':
                        url1 = f'https://bonbanh.com/oto/suzuki-{button23}'
                else:
                        url1 = f'https://bonbanh.com/oto/suzuki-khac'

        elif tag_brand == 'Toyota':
                button24 = st.sidebar.radio('Toyota', ['Vios','Fortuner','Innova','Camry','Corolla altis','Corolla Cross','Land Cruiser','Yaris','Prado','Veloz', 
                                                        'Wigo','Hilux','Raize','Sienna','4 Runner','86','Allion','Alphard','Altezza','Aristo','Aurion','Avalon','Avanza', 
                                                        'Avensis','Aygo','Blizzard','Brevis','C-HR','Caldina','Cami','Carina','Celica','Century','Chaser','Corolla','Corolla verso', 
                                                        'Corona','Corsa','Cressida','Cresta','Crown','Cynos','Estima','Fj cruiser','Gaia','Granvia','Harrier','Hiace','Highlander', 
                                                        'Ipsum','IQ','Liteace','Mark II','Matrix','Mega cruiser','MR 2','Picnic','Platz','Premio','Previa','Prius','Progres','Pronard','Raum', 
                                                        'RAV4','Rush','Scepter','Sequoia','Sera','Soarer','Solara','Starlet','Supra','Tacoma','Tercel','Townace','Tundra','Van','Venza','Verossa',
                                                        'Verso','Vista','Windom','Wish','XA','Yaris Cross','Yaris Verso','Zace', 'Other'])
                                                
                if button24 != 'Other':
                        url1 = f'https://bonbanh.com/oto/toyota-{button24}'
                else:
                        url1 = f'https://bonbanh.com/oto/toyota-khac'
                
        elif tag_brand == 'VinFast':
                button25 = st.sidebar.radio('VinFast', ['Fadil','Lux A 2.0','Lux SA 2.0','VF8','VF5','VF9','VF e34','President','VF3','VF6','VF7'])                        
                url1 = f'https://bonbanh.com/oto/toyota-{button25}'
                
        elif tag_brand == 'Volkswagen':
                button26 = st.sidebar.radio('Volkswagen', ['Teramont','Tiguan','Touareg','Polo','T-Cross','Virtus','Beetle','Bora','Caddy','California','Corrado', 
                                                                'Crafter','Derby','Eos','Golf','Golf Plus','Jetta','Multivan','New Beetle','Passat','Phaeton','Routan',
                                                                'Scirocco','Sharan','Solo','Transporter','Vento','Viloran', 'Other'])
                                                
                if button26 != 'Other':
                        url1 = f'http s://bonbanh.com/oto/volkswagen-{button26}'
                else:
                        url1 = f'https://bonbanh.com/oto/volkswagen-khac'

        elif tag_brand == 'Volvo':
                button27 = st.sidebar.radio('Volvo', ['XC90','XC60','S90','XC40','V60','S60','264','340 360','460','740','760','850','940','960','C70','S40', 
                                                        'Torslanda','V70','V90','XC70', 'Other'])
                                                
                if button27 != 'Other':
                        url1 = f'https://bonbanh.com/oto/volvo-{button27}'
                else:
                        url1 = f'https://bonbanh.com/oto/volvo-khac'
                        
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

                st.success(model)
                left_column, right_column = st.columns(2)
                with right_column:
                    status = car.find("div", class_="cb1").text
                    price = car.find("div", class_="cb3").text

                    split_price = price.split()
                    if 'Tỷ' in split_price:
                        if 'Triệu' in split_price:
                            new_price = int(split_price[split_price.index('Tỷ') - 1]) * 1000 + int(split_price[split_price.index('Tỷ') + 1])
                        else:
                            new_price = int(split_price[split_price.index('Tỷ') - 1])
                    elif 'Triệu' in split_price:
                        new_price = int(split_price[split_price.index('Triệu') - 1])

                    location = car.find("div", "cb4").text
                    discript = car.find("div", class_="cb6_02").text
                    contact = car.find("div", class_="cb7").text
                    st.write(status)
                    st.write(price)
                    st.write(location) 
                    st.write(discript)
                    st.write(contact)
                with left_column:
                    car_img = car.find('div', class_="cb5")
                    car_img = car.find('img')
                    car_img = car_img.get('src') 
                    if 'https' not in car_img:
                        st.write('No Picture')
                    else:
                        st.image(car_img)
            all_info.append([car_brand, car_name, year_of_manufacture, new_price])
        

with tab2:
    df = pd.DataFrame(all_info, columns=['Brand', 'Name', 'Year of manufacture', 'Price'])
    #df.to_csv('car_data.csv')

    st.dataframe(df)
    st.bar_chart(df['Brand'].value_counts())
    st.bar_chart(df['Year of manufacture'].value_counts())