import pandas as pd
import streamlit as st

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

        elif tag_brand == 'Audi':
            button1 = st.sidebar.selectbox('Audi', ['All','Q5','Q7', 'A6', 'A4', 'A8', 'A5', 'Q8', 'Q2', 'A7', '100', '200',
                                                    '80', '90', 'A1', 'A2', 'A3', 'Cabriolet', 'Coupe', 'E-tron',
                                                    'E-tron GT','Q3','Quattro','R8','RS2','RS4', 'S5','S8','TT','V8'])
            if button1 != 'All':
                data = search_tool(f'Audi {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Bentley':
            button1 = st.sidebar.selectbox('Bentley', ['All','Flying Spur', 'Mulsanne', 'Bentayga', 'Continental', 'Arnage',
                                            'Azure', 'Brooklands', 'Turbo'])
                                            
            if button1 != 'All':
                data = search_tool(f'Bentley {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
            
        elif tag_brand == 'BMW':
            button1 = st.sidebar.selectbox('BMW', ['All','3 Series', '5 Series', '7 Series', 'X3', 'X6', 'X5', '4 Series', 
                                                    'X7', 'Z4', '1 Series', '2 Series', '6 Series', '8 Series', 'Alpina',
                                                    'i3', 'i8', 'iX', 'iX3', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M8', 'X1',
                                                    'X2', 'X4', 'XM', 'Z3', 'Z8'])               
            if button1 != 'All':
                data = search_tool(f'BMW {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]

        elif tag_brand == 'Chevrolet':
            button1 = st.sidebar.selectbox('Chevrolet', ['All','Spark', 'Cruze', 'Captiva', 'Colorado', 'Aveo', 'Trailblazer', 
                                                            'Vivant', 'Orlando', 'Camaro', 'Trax', 'Lacetti', 'Alero', 'Astro', 
                                                            'Avanlanche', 'Beretta', 'Caprice', 'Cavalier', 'Chevyvan' ,'Cobalt',
                                                            'Corsica', 'Corvette', 'Equinox', 'Explorer', 'Express', 'Impala',
                                                            'Ipanema', 'Kalos', 'Lumina', 'Malibu', 'Matiz', 'Nubira', 'Prizm',
                                                            'S 10', 'Silverado', 'Spectrum', 'SSR', 'Suburban', 'Tahoe', 'Tracker',
                                                            'Trans Sport', 'Venture'])
                                            
            if button1 != 'All':
                data = search_tool(f'Chevrolet {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
            
        elif tag_brand == 'Daewoo':
            button1 = st.sidebar.selectbox('Daewoo', ['All','Lacetti', 'Matiz', 'Gentra', 'Lanos', 'Nubira', 'Magnus', 'GentraX',
                                                    'Damas', 'Aranos', 'Arcadia', 'Brougham', 'Chairman', 'Cielo', 'Espero',
                                                    'Evanda', 'Istana', 'Kalos', 'Korando', 'Labo', 'Leganza', 'Lublin',
                                                    'Musso', 'Nexia', 'Novus', 'Polonez', 'Prince', 'Racer', 'Rexton',
                                                    'Rezzo', 'Statesman', 'Super Saloon', 'Tacuma', 'Tico', 'Tosca', 'Winstorm'])
                                            
            if button1 != 'All':
                data = search_tool(f'Daewoo {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Ford':
            button1 = st.sidebar.selectbox('Ford', ['All','Ranger', 'Everest', 'Territory', 'EcoSport', 'Transit', 'Focus', 
                                                    'Fiesta', 'Escape', 'Explorer', 'Tourneo', 'Acononline', 'Aerostar', 
                                                    'Aspire', 'Bronco', 'Capri', 'Caravan', 'Cargo', 'Club wagon', 'Contour',
                                                    'Courier', 'Crown victoria', 'E450', 'Edge', 'Escort', 'EscurSeon',
                                                    'Expedition', 'Express', 'F150', 'F250', 'F350', 'F450', 'F700', 'Flex',
                                                    'Focus C Max', 'Fusion', 'Galaxie', 'Imax', 'Ka', 'Laser', 'Maverick',
                                                    'Mondeo', 'Mustang', 'Orion', 'Pinto', 'Probe', 'Puma', 'Sierra', 'Streetka',
                                                    'Taurus', 'Tempo', 'Windstar'])
                                            
            if button1 != 'All':
                data = search_tool(f'Ford {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Honda':
            button1 = st.sidebar.selectbox('Honda', ['All','CRV', 'City', 'Civic', 'HRV', 'Brio', 'BR V', 'Accord', 'Jazz',
                                                    'Odyssey', 'Capa', 'Concerto', 'CR X', 'CR Z', 'Domani', 'Element',
                                                    'FIT', 'FR V', 'Insight', 'Inspire', 'Integra', 'Legend', 'Life',
                                                    'Mobilo', 'NSX', 'Passport', 'Pilot', 'Prelude', 'S2000', 'Saber',
                                                    'Shuttle', 'Stream', 'Today', 'Torneo', 'Vigor', 'Z'])
                                            
            if button1 != 'All':
                data = search_tool(f'Honda {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 

        elif tag_brand == 'Hyundai':
            button1 = st.sidebar.selectbox('Hyundai', ['All','Custin','Palisade','i10','SantaFe','Accent','Tucson','Elantra', 
                                                    'Kona','Creta','Getz','Stargazer','Avante','Atos','Azera','Centennial','Click', 
                                                    'County','Coupe','Custo','Dynasty','eMighty','Eon','Equus','Excel','Galloper', 
                                                    'Genesis','Gold','Grace','Grand Starex','Grandeur','H 1','H 100','H350','HD','i20', 
                                                    'i30','i40','Innovation','Ioniq 5','Lantra','Lavita','Libero','Marcia', 
                                                    'Matrix','Maxcruz','Mighty','Pony','Porter','S coupe','Santa Cruz','Santamo','Solati', 
                                                    'Sonata','Starex','Terracan','Tiburon','Trajet','Tuscani','Universe','Universe Xpress Luxury', 
                                                    'Veloster','Veracruz','Verna','Xcent','XG'])
                                            
            if button1 != 'All':
                data = search_tool(f'Hyundai {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Isuzu':
            button1 = st.sidebar.selectbox('Isuzu', ['All','Dmax','MU-X','QKR','Hi lander','NQR','NPR','Amigo','Ascender','Aska', 
                                                    'AXiom','Campo','D Cargo','Faster','FVR','Gemini','Midi','MU','NLR','NMR', 
                                                    'Panther','Pick up','Rodeo','Trooper','Turkuaz','Vehi cross','Wi zard'])
                                            
            if button1 != 'All':
                data = search_tool(f'Isuzu {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 

        elif tag_brand == 'Jeep':
            button1 = st.sidebar.selectbox('Jeep', ['All','Wrangler','Gladiator','A2','Cherokee','Grand cherokee','Liberty','CJ',
                                                    'Compass','Grand Wagoneer'])
                                            
            if button1 != 'All':
                data = search_tool(f'Jeep {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]

        elif tag_brand == 'Kia':
            button1 = st.sidebar.selectbox('Kia', ['All','Morning','Cerato','Carnival','K3','Sorento','Seltos','Sedona','Rio', 
                                                    'Carens','Soluto','Sonet','Forte','Avella','Bongo','Cadenza','Clarus','Concord', 
                                                    'Credos','Elan','Enterprise','Frontier','Jeep','Joice','K2700','K3000S','K4','K5', 
                                                    'K7','Lotze','Magentis','Opirus','Optima','Picanto','Potentia','Pregio','Pride',
                                                    'Quoris','Ray','Retona','Roadster','Rondo','Sephia','Shuma','Soul','Spectra', 
                                                    'Sportage','Visto','X Trek'])
                                            
            if button1 != 'All':
                data = search_tool(f'Kia {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                        
        elif tag_brand == 'LandRover':
            button1 = st.sidebar.selectbox('LandRover', ['All','Range Rover','Range Rover Evoque','Range Rover Sport', 
                                                            'Range Rover Velar','Defender','Discovery Sport','Discovery', 
                                                            'Freelander'])
                                            
            if button1 != 'All':
                data = search_tool(f'LandRover {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Lexus':
            button1 = st.sidebar.selectbox('Lexus', ['All','LX','RX','ES','GX','LS','NX','IS','GS','CT','HS','LC','LM','RC','SC','SL'])
                                            
            if button1 != 'All':
                data = search_tool(f'Lexus {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]   
               
        elif tag_brand == 'Mazda':
            button1 = st.sidebar.selectbox('Mazda', ['All','3','CX5','6','2','BT50','CX8','cx3','CX 30','323','626','1','323F',
                                                    '5','929','Atenza','AZ','B series','Bongo Friendee','Carol','Cronos','CX7', 
                                                    'CX9','Eunos','Familia','Millenia','MPV','MX 3','MX 5','MX 6','Pickup','Premacy', 
                                                    'RX 7','RX 8','Tribute','Xedos 9'])
                                            
            if button1 != 'All':
                data = search_tool(f'Mazda {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]  
                
        elif tag_brand == 'Mercedes':
            button1 = st.sidebar.selectbox('Mercedes Benz', ['All','GLC','C class','E class','S class','Maybach','G class','GLS', 
                                                            'GLE Class','GLB','190','A class','AMG GT','Atego','B class', 
                                                            'CL class','CLA class','CLK class','CLS class','EQB','EQE','EQS', 
                                                            'GL','GLA class','GLK Class','M class','MB','ML Class','R class', 
                                                            'SL class','SLC','SLK class','SLR Mclaren','Sprinter','SR class', 
                                                            'V class','Vaneo','Viano','Vito'])
                                            
            if button1 != 'All':
                data = search_tool(f'Mercedes Benz {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]  

        elif tag_brand == 'MG':
            button1 = st.sidebar.selectbox('MG', ['All','5','ZS','HS','X','ZT','MGF','3','350C','6','Express','RX5'])
                                            
            if button1 != 'All':
                data = search_tool(f'MG {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 

        elif tag_brand == 'Mini':
            button1 = st.sidebar.selectbox('Mini', ['All','Cooper','One'])
                                            
            if button1 != 'All':
                data = search_tool(f'Mini {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 

        elif tag_brand == 'Mitsubishi':
            button1 = st.sidebar.selectbox('Mitsubishi', ['All','Xpander','Triton','Attrage','Outlander','Pajero Sport','Pajero', 
                                                            'Jolie','Mirage','Grandis','Lancer','Zinger','Outlander Sport','3000GT', 
                                                            'Airtek','Canter','Carisma','Challenger','Chariot','Colt','Delica', 
                                                            'Diamante','Dion','Eclipse','EK wagon','FTO','Galant','Grunder','GTO', 
                                                            'Hover','IO','Jeep','L200','L300','L400','Libero','Minica','Montero', 
                                                            'Pinin','Santamo','Savrin','Sigma','Space Gear','Space wagon','Starion', 
                                                            'Veryca','Xforce'])
                                            
            if button1 != 'All':
                data = search_tool(f'Mitsubishi {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Nissan':
            button1 = st.sidebar.selectbox('Nissan', ['All','Navara','X trail','Almera','Sunny','Teana','Terra','Kicks','Grand livina', 
                                                    'Bluebird','Murano','Maxima','Qashqai','100NX','200SX','240SX','300ZX','350Z', 
                                                    '370Z','Altima','Armada','Avenir','Bassara','Cedric','Cefiro','Cima','Elgrand', 
                                                    'Frontier','Gloria','GT R','Juke','Langley','Largo','Laurel','Leaf','Liberty', 
                                                    'Livina','Micra','Moco','NV','Pathfinder','Patrol','Pick up','Pixo','Prairie', 
                                                    'Presage','Presea','President','Primastar','Primera','Pulsar','Quest','Rasheen', 
                                                    'Rogue','Safari','Sentra','Serena','Silvia','Skyline','Stagea','Stanza','Terrano', 
                                                    'Tiida','Tino','Urvan','Vanette','Versa','Wingroad','X Terra'])
                                    
            if button1 != 'All':
                data = search_tool(f'Nissan {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Peugeot':
            button1 = st.sidebar.selectbox('Peugeot', ['All','3008','2008','5008','408','Traveller','208','107','205','206', 
                                                            '207','305','306','307','308','309','404','405','406','407','504', 
                                                            '505','508','605','607','807','Boxer','J5','RCZ'])
                                            
            if button1 != 'All':
                data = search_tool(f'Peugeot {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 

        elif tag_brand == 'Porsche':
            button1 = st.sidebar.selectbox('Porsche', ['All','Cayenne','Panamera','Macan','718','911','Taycan','928','944', 
                                                            '968','Boxster','Carrera','Cayman'])
                                            
            if button1 != 'All':
                data = search_tool(f'Porsche {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                        
        elif tag_brand == 'Subaru':
            button1 = st.sidebar.selectbox('Subaru', ['All','Forester','Outback','BRZ','WRX','Tutto','Levorg','Dex','Impreza', 
                                                    'Legacy','Tribeca','XV'])
                                            
            if button1 != 'All':
                data = search_tool(f'Subaru {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Suzuki':
            button1 = st.sidebar.selectbox('Suzuki', ['All','Swift','XL7','Super Carry Van','Ertiga','Super Carry Truck','Carry','Aerio', 
                                                    'Alto','APV','Baleno','Celerio','Ciaz','Cultis wagon','Esteem','Every landy', 
                                                    'Grand vitara','Jimmy','Kei','Liana','Samurai','SJ','SX4','Twin','Vitara','Wagon R+','X90'])
                                            
            if button1 != 'All':
                data = search_tool(f'Suzuki {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 

        elif tag_brand == 'Toyota':
            button1 = st.sidebar.selectbox('Toyota', ['All','Vios','Fortuner','Innova','Camry','Corolla altis','Corolla Cross','Land Cruiser','Yaris','Prado','Veloz', 
                                                    'Wigo','Hilux','Raize','Sienna','4 Runner','86','Allion','Alphard','Altezza','Aristo','Aurion','Avalon','Avanza', 
                                                    'Avensis','Aygo','Blizzard','Brevis','C-HR','Caldina','Cami','Carina','Celica','Century','Chaser','Corolla','Corolla verso', 
                                                    'Corona','Corsa','Cressida','Cresta','Crown','Cynos','Estima','Fj cruiser','Gaia','Granvia','Harrier','Hiace','Highlander', 
                                                    'Ipsum','IQ','Liteace','Mark II','Matrix','Mega cruiser','MR 2','Picnic','Platz','Premio','Previa','Prius','Progres','Pronard','Raum', 
                                                    'RAV4','Rush','Scepter','Sequoia','Sera','Soarer','Solara','Starlet','Supra','Tacoma','Tercel','Townace','Tundra','Van','Venza','Verossa',
                                                    'Verso','Vista','Windom','Wish','XA','Yaris Cross','Yaris Verso','Zace'])
                                            
            if button1 != 'All':
                data = search_tool(f'Toyota {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'VinFast':
            button1 = st.sidebar.selectbox('VinFast', ['All','Fadil','Lux A 2.0','Lux SA 2.0','VF8','VF5','VF9','VF e34','President','VF3','VF6','VF7'])       
            if button1 != 'All':
                data = search_tool(f'VinFast {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Volkswagen':
            button1 = st.sidebar.selectbox('Volkswagen', ['All','Teramont','Tiguan','Touareg','Polo','T-Cross','Virtus','Beetle','Bora','Caddy','California','Corrado', 
                                                            'Crafter','Derby','Eos','Golf','Golf Plus','Jetta','Multivan','New Beetle','Passat','Phaeton','Routan',
                                                            'Scirocco','Sharan','Solo','Transporter','Vento','Viloran'])
                                            
            if button1 != 'All':
                data = search_tool(f'Volkswagen {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Volvo':
            button1 = st.sidebar.selectbox('Volvo', ['All','XC90','XC60','S90','XC40','V60','S60','264','340 360','460','740','760','850','940','960','C70','S40', 
                                                    'Torslanda','V70','V90','XC70'])
                                            
            if button1 != 'All':
                data = search_tool(f'Volvo {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
        
                
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
