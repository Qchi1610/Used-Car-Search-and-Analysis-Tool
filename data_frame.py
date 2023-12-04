import pandas as pd
import streamlit as st


def reset():
    st.session_state['Search'] = False
    st.session_state['brand'] = 'All' 
    st.session_state['year'] = 'All'
    st.session_state['price'] = [0, 2000]

def data_table(tag_brand, tag_year, tag_price, all_data): 
    data = all_data
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

        
        elif tag_brand == 'Acura':
            button1 = st.sidebar.selectbox('Acura', ['All', 'MDX','ZDX','RDX','TSX','CL','Legend','EL','ILX','Integra','NSX','RL','RSX','SLX','TL','Vigor'])

            if button1 != 'All':
                data = search_tool(f'Acura {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Alfa Romeo':
            button1 = st.sidebar.selectbox('Alfa Romeo', ['All', '159','GT','Spider'])

            if button1 != 'All':
                data = search_tool(f'Alfa Romeo {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == 'Alfa']
        
        elif tag_brand == 'Aston Martin':
            button1 = st.sidebar.selectbox('Aston Martin', ['All', 'DB11','DB7','DB9','Lagonda','Rapide','Vanquish','Vantage','Virage','Volante','Zagato'])

            if button1 != 'All':
                data = search_tool(f'Aston Martin {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == 'Aston']
                
        elif tag_brand == 'Baic':
            button1 = st.sidebar.selectbox('Baic',['Beijing X7','Q7','Beijing U5','F6','BJ40','X55','A5','B90W Concept','BJ100 Concept','C50E','C60F','C90L','Concept 900', 
                                                    'CX51','D50','D60','D70','D80','Doda','F5','H2','S3','S6','V2','X25','X35','X65','CC'])

            if button1 != 'All':
                data = search_tool(f'Baic {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Brilliance':
            button1 = st.sidebar.selectbox('Brilliance', ['All', 'V3','V5','V6','V7'])

            if button1 != 'All':
                data = search_tool(f'Brilliance {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Cadillac':
            button1 = st.sidebar.selectbox('Cadillac', ['All', 'Escalade','CTS','SRX','Allante','ATS','STS','Catera','CT6','Deville','Eldorado', 
                                                        'Fleetwood','LSE','Seville','Vizon','XLR'])

            if button1 != 'All':
                data = search_tool(f'Cadillac {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
        
        elif tag_brand == 'Changan':
            button1 = st.sidebar.selectbox('Changan', ['All', 'CS35','CX20','CX30','Eado','G50','Honor'])

            if button1 != 'All':
                data = search_tool(f'Changan {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Chery':
            button1 = st.sidebar.selectbox('Chery', ['All', 'A3','Apola','QQ3','Riich'])

            if button1 != 'All':
                data = search_tool(f'Chery {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
        
        elif tag_brand == 'Chrysler':
            button1 = st.sidebar.selectbox('Chrysler', ['All', '300C','LeBaron','Grand Voyager','Voyager','200','Town & Country','300M','Cirus','Concorde','Crossfire','Cruiser', 
                                                        'Daytona Shelby','Intrepid','Jeep cherokee','Jeep Grande Cherokee','LHS','Limiter','Neon','New Yorker','Pacifica', 
                                                        'Prowler','PT Cruiser','Saratoga','Sebring','Stratus','Vipen','Vision'])

            if button1 != 'All':
                data = search_tool(f'Chrysler {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
        
        elif tag_brand == 'Citroen':
            button1 = st.sidebar.selectbox('Citroen', ['All', 'AX','Berlingo''BX','C1','C15','C2','C3','C4','C5','C8','CX','DS3','Evasion', 
                                                        'JumPer','Jumpy','Saxo','Sinergie','Visa','Xantia','XM','Xsara','Xsara Pacasso','ZX'])

            if button1 != 'All':
                data = search_tool(f'Citroen {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Daihatsu':
            button1 = st.sidebar.selectbox('Daihatsu', ['All', 'Terios','Citivan','Feroza','Charade','Hijet','Sirion','Applause','Compagno','Fellow Max','Materia'])

            if button1 != 'All':
                data = search_tool(f'Daihatsu {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]     
                
        elif tag_brand == 'Dodge':
            button1 = st.sidebar.selectbox('Dodge', ['All', 'Avenger','Caliber','Caravan','Challenger','Charger','Dakota','Durango','Grand caravan','Intrepid', 
                                                        'Journey','Magnum','Neon','Nitro','Ram','Spirit','Stealth','Stratus','Viper','Voyager'])

            if button1 != 'All':
                data = search_tool(f'Dodge {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Dongben':
            button1 = st.sidebar.selectbox('Dongben', ['All', 'DB X30','DB1021','SRM T20','SRM X30'])

            if button1 != 'All':
                data = search_tool(f'Dongben {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Dongfeng':
            button1 = st.sidebar.selectbox('Dongfeng', ['All', 'Fengxing CM7','Forthing T5','Future','Glory','Joyear S50','Joyear T5','Joyear X5','Lingzhi M3','SX6'])

            if button1 != 'All':
                data = search_tool(f'Dongfeng {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Ferrari':
            button1 = st.sidebar.selectbox('Ferrari', ['All', '488','SF90 Stradale','F12','Roma','F8','California','360 Modena','456','458','550','575','612','812', 
                                                        'Barchetta','Enze','F 355','F 360','F 430','F 50','F 512','GTC4Lusso','Maranello','Mondial','Monza','Portofino','Testarossa'])

            if button1 != 'All':
                data = search_tool(f'Ferrari {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Fiat':
            button1 = st.sidebar.selectbox('Fiat', ['All', '500','Siena','Albea','Doblo','Seicento','Strada','126','Bachetta','Brava','Bravo','Cinquecento','Coupe','Croma','Ducato', 
                                                    'Duna','Fiorino','Idea','Marea','Marengo','Multipla','Panda','Pario','Punto','Regata','Ritmo','Scudo','Stilo','Talento', 
                                                    'Tempra','Tipo','Ulysse','Uno','X1/9'])

            if button1 != 'All':
                data = search_tool(f'Fiat {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]                                  
        
        elif tag_brand == 'GMC':
            button1 = st.sidebar.selectbox('GMC', ['All', 'Envoy','Hummer','Jimmy','Savana','Sierra','Sonuna','Tracker','Yukon'])

            if button1 != 'All':
                data = search_tool(f'GMC {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Haima':
            button1 = st.sidebar.selectbox('Haima', ['All', '2','3','Freema','7','Fstar','M3','M8','S5','S7','V70'])

            if button1 != 'All':
                data = search_tool(f'Haima {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Haval':
            button1 = st.sidebar.selectbox('Haval', ['All', 'H6'])

            if button1 != 'All':
                data = search_tool(f'Haval {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]  
                
        elif tag_brand == 'Hino':
            button1 = st.sidebar.selectbox('Hino', ['All', '500 Series','300 Series','700 Series'])

            if button1 != 'All':
                data = search_tool(f'Hino {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]   
                
        elif tag_brand == 'Hongqi':
            button1 = st.sidebar.selectbox('Hongqi', ['All', 'E-HS9','H9'])

            if button1 != 'All':
                data = search_tool(f'Hongqi {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]    

        elif tag_brand == 'Hummer':
            button1 = st.sidebar.selectbox('Hummer', ['All', 'H1','H2','H3'])

            if button1 != 'All':
                data = search_tool(f'Hummer {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]

        elif tag_brand == 'Infiniti':
            button1 = st.sidebar.selectbox('Infiniti', ['All', 'QX','EX','Q45','G37','FX','G20','G35','I20','I35','J30','JX','M30','Q30'])

            if button1 != 'All':
                data = search_tool(f'Infiniti {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Jaguar':
            button1 = st.sidebar.selectbox('Jaguar', ['All', 'XJ series','F-Pace','XF','F Type','XE','E Type','E-Pace','I-Pace','S Type','Sovereign','X Type','XK series'])

            if button1 != 'All':
                data = search_tool(f'Jaguar {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]    
                
        elif tag_brand == 'JRD':
            button1 = st.sidebar.selectbox('JRD', ['All', 'Daily','Manjia','Mega','Travel'])

            if button1 != 'All':
                data = search_tool(f'JRD {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]            

        elif tag_brand == 'Lamborghini':
            button1 = st.sidebar.selectbox('Lamborghini', ['All', 'Urus','Huracan','Aventador','Diablo','Gallado','Murcielago'])

            if button1 != 'All':
                data = search_tool(f'Lamborghini {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Lifan':
            button1 = st.sidebar.selectbox('Lifan', ['All', '320','520','620'])

            if button1 != 'All':
                data = search_tool(f'Lifan {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Lincoln':
            button1 = st.sidebar.selectbox('Lincoln', ['All', 'Navigator','Aviator','Continental','Town car','Corsair','Nautilus','Blackwood','LX','Mart VIII','MKC','MKZ'])

            if button1 != 'All':
                data = search_tool(f'Lincoln {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]                                                                                                                   

        elif tag_brand == 'Luxgen':
            button1 = st.sidebar.selectbox('Luxgen', ['All', '5','7 MPV','7 SUV','M7','S3','S5','U6','U7'])

            if button1 != 'All':
                data = search_tool(f'Luxgen {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]

        elif tag_brand == 'Maserati':
            button1 = st.sidebar.selectbox('Maserati', ['All', 'Levante','Ghibli','Quattroporte','MC20','GranTurismo','GranCabrio','3200GT','Biturbo','Gransport','Grecale','Spyder'])

            if button1 != 'All':
                data = search_tool(f'Maserati {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Maybach':
            button1 = st.sidebar.selectbox('Maybach', ['All', '57', '62'])

            if button1 != 'All':
                data = search_tool(f'Maybach {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'McLaren':
            button1 = st.sidebar.selectbox('McLaren', ['All', '650s','720S','765LT','570S','12C','540C','570GT','600LT','675LT','F1','M6GT','P1','Senna','speedtail'])

            if button1 != 'All':
                data = search_tool(f'McLaren {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Mekong':
            button1 = st.sidebar.selectbox('Mekong', ['All', 'Paso','Premio','Pronto','Star'])

            if button1 != 'All':
                data = search_tool(f'Mekong {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]                                                       

        elif tag_brand == 'Morgan':
            button1 = st.sidebar.selectbox('Morgan', ['All', 'Plus Four', 'Plus Six'])

            if button1 != 'All':
                data = search_tool(f'Morgan {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
        
        elif tag_brand == 'RAM':
            button1 = st.sidebar.selectbox('RAM', ['All', '1500','2500','3500'])

            if button1 != 'All':
                data = search_tool(f'RAM {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
        
        elif tag_brand == 'Renault':
            button1 = st.sidebar.selectbox('Renault', ['All', 'Kaptur','21','Duster','Clio','Latitude','Koleos','11','19','25','4','9','Arkana','Avantime','Espace', 
                                                        'Express','Fluence','Grand Espace','Kangoo','Laguna','Logan','Magnum','Master','Megane','Modus','Rapid', 
                                                        'Safrane','Sandero','Scenic','Sport Spider','Super 5','Symbol','Talisman','Thalia','Trafic','Twingo','Vel satis','Wind'])

            if button1 != 'All':
                data = search_tool(f'Renault {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'Rolls Royce':
            button1 = st.sidebar.selectbox('Rolls Royce', ['All', 'Ghost','Cullinan','Phantom','Silver','Corniche','Park ward','Dawn','Wraith'])

            if button1 != 'All':
                data = search_tool(f'Rolls Royce {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == 'Rolls'] 
                
        elif tag_brand == 'Samsung':
            button1 = st.sidebar.selectbox('Samsung', ['All', 'QM5','SM3','SM5','SM7'])

            if button1 != 'All':
                data = search_tool(f'Samsung {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand] 
                
        elif tag_brand == 'Scion':
            button1 = st.sidebar.selectbox('Scion', ['All', 'FR-S','Tc','Xb','Xd'])

            if button1 != 'All':
                data = search_tool(f'Scion {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]                                      

        elif tag_brand == 'Skoda':
            button1 = st.sidebar.selectbox('Skoda', ['All', 'Enyaq iV','Fabia','Kamiq','Karoq','Kodiaq','Octavia','Scala','Superb'])

            if button1 != 'All':
                data = search_tool(f'Skoda {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]                                                                        

        elif tag_brand == 'Smart':
            button1 = st.sidebar.selectbox('Smart', ['All', 'City','Coupe','Crossblade','Forfour','Fortwo','MCC','Roadster'])

            if button1 != 'All':
                data = search_tool(f'Smart {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]

        elif tag_brand == 'Ssangyong':
            button1 = st.sidebar.selectbox('Ssangyong', ['All', 'Tivoli','Korando','Musso','Rexton','Stavic','Korando Sport','Actyon','Chairman','Family','Istana','Kalista','Kyron','XLV'])

            if button1 != 'All':
                data = search_tool(f'Ssangyong {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]
                
        elif tag_brand == 'SYM':
            button1 = st.sidebar.selectbox('SYM', ['All', 'T1000','T880','V11','V5'])

            if button1 != 'All':
                data = search_tool(f'SYM {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]                        

        elif tag_brand == 'Thaco':
            button1 = st.sidebar.selectbox('Thaco', ['All', 'Towner','Frontier','Ollin','Forland','Foton','Auman','Aumark','Mobihome','Town'])

            if button1 != 'All':
                data = search_tool(f'Thaco {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]

        elif tag_brand == 'Tobe':
            button1 = st.sidebar.selectbox('Tobe', ['All', 'Mcar'])

            if button1 != 'All':
                data = search_tool(f'Tobe {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]                        

        elif tag_brand == 'UAZ':
            button1 = st.sidebar.selectbox('UAZ', ['All', 'Hunter','Patriot','Pickup','Simbir'])

            if button1 != 'All':
                data = search_tool(f'UAZ {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]

        elif tag_brand == 'Vinaxuki':
            button1 = st.sidebar.selectbox('Vinaxuki', ['All', '1240T','Jinbei','1200B','Hafei','5500TL','990T','1490T','1980T','1990BA','2500BA', 
                                                        '3000BA','3450T','3500TL','3500TL','4500BA','4500BABD','5000BA','7000BA','8500TL'])

            if button1 != 'All':
                data = search_tool(f'Vinaxuki {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]

        elif tag_brand == 'Wuling':
            button1 = st.sidebar.selectbox('Wuling', ['All', 'Brilliance','Brilliance Van','Hongguang','Hongguang MiniEV','Sunshine'])

            if button1 != 'All':
                data = search_tool(f'Wuling {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]

        elif tag_brand == 'Zotye':
            button1 = st.sidebar.selectbox('Zotye', ['All', 'Z8','T600','T300','Z100','Z300','Z500','Hunter'])

            if button1 != 'All':
                data = search_tool(f'Zotye {button1}', all_data)
            else:
                data = all_data[all_data['Brand'] == tag_brand]

        elif tag_brand != 'All':
            data = all_data[all_data['Brand'] == tag_brand]

        if tag_year != 'All':
            data = data[data['Year of manufacture'] == str(tag_year)]
        

    if tag_price[0] != 0 and tag_price[1] != 2000:
        data = data[(data['Gia so'] >= tag_price[0]) & (data['Gia so'] <= tag_price[1])]
    
    elif tag_price[0] != 0:
        data = data[data['Gia so'] >= tag_price[0]]

    elif tag_price[1] != 2000:
        data = data[data['Gia so'] <= tag_price[1]]

    return data

def search_tool(regex: str, df):
    textlikes = df.select_dtypes(include=[object])
    return df[textlikes.apply(lambda column: column.str.contains(regex, regex=False, case = False, na=False)).any(axis = 1)]
