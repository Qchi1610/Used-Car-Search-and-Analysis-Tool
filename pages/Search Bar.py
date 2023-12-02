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

if tag_brand == 'All' and tag_year == 'All' and tag_price[0] == 0 and tag_price[1] == 2000:
    url1 = 'https://bonbanh.com/oto-cu-da-qua-su-dung'
else:
        if tag_brand == 'Other [+]':
                other_brand = st.radio('Other brand', ['Acura','Alfa Romeo','Aston Martin','Baic','Brilliance','Cadillac','Changan','Chery','Chrysler','Citroen','Daihatsu',
                                'Dodge','Dongben','Dongfeng','Ferrari','Fiat','GMC','Haima','Haval','Hino','Hongqi','Hummer','Infiniti','Jaguar',
                                'JRD','Lamborghini','Lifan','Lincoln','Luxgen','Maserati','Maybach','McLaren','Mekong','Morgan','RAM','Renault',
                                'Rolls Royce','Samsung','Scion','Skoda','Smart','SYM','Thaco','Tobe','Ssangyong','UAZ','Vinaxuki','Wuling','Zotye', 'Other'])
        
                if other_brand == 'Acura':
                        button1 = st.sidebar.radio('Acura', ['MDX','ZDX','RDX','TSX','CL','Legend','EL','ILX','Integra','NSX','RL','RSX','SLX','TL','Vigor'])
                        
                elif other_brand == 'Alfa Romeo':
                        button1 = st.sidebar.radio('Alfa Romeo', ['159','GT','Spider'])
                
                elif other_brand == 'Aston Martin':
                        button1 = st.sidebar.radio('Aston Martin', ['DB11','DB7','DB9','Lagonda','Rapide','Vanquish','Vantage','Virage','Volante','Zagato'])
                        
                elif other_brand == 'Baic':
                        button1 = st.sidebar.radio('Baic',['Beijing X7','Q7','Beijing U5','F6','BJ40','X55','A5','B90W Concept','BJ100 Concept','C50E','C60F','C90L','Concept 900', 
                                                           'CX51','D50','D60','D70','D80','Doda','F5','H2','S3','S6','V2','X25','X35','X65','CC']) 
                      
                elif other_brand == 'Brilliance':
                        button1 = st.sidebar.radio('Brilliance', ['V3','V5','V6','V7'])
                        
                elif other_brand == 'Cadillac':
                        button1 = st.sidebar.radio('Cadillac', ['Escalade','CTS','SRX','Allante','ATS','STS','Catera','CT6','Deville','Eldorado', 
                                                                'Fleetwood','LSE','Seville','Vizon','XLR'])
                
                elif other_brand == 'Changan':
                        button1 = st.sidebar.radio('Changan', ['CS35','CX20','CX30','Eado','G50','Honor'])
                        
                elif other_brand == 'Chery':
                        button1 = st.sidebar.radio('Chery', ['A3','Apola','QQ3','Riich'])
                
                elif other_brand == 'Chrysler':
                        button1 = st.sidebar.radio('Chrysler', ['300C','LeBaron','Grand Voyager','Voyager','200','Town & Country','300M','Cirus','Concorde','Crossfire','Cruiser', 
                                                                'Daytona Shelby','Intrepid','Jeep cherokee','Jeep Grande Cherokee','LHS','Limiter','Neon','New Yorker','Pacifica', 
                                                                'Prowler','PT Cruiser','Saratoga','Sebring','Stratus','Vipen','Vision'])
                
                elif other_brand == 'Citroen':
                        button1 = st.sidebar.radio('Citroen', ['AX','Berlingo''BX','C1','C15','C2','C3','C4','C5','C8','CX','DS3','Evasion', 
                                                               'JumPer','Jumpy','Saxo','Sinergie','Visa','Xantia','XM','Xsara','Xsara Pacasso','ZX']) 
                        
                elif other_brand == 'Daihatsu':
                        button1 = st.sidebar.radio('Daihatsu', ['Terios','Citivan','Feroza','Charade','Hijet','Sirion','Applause','Compagno','Fellow Max','Materia'])     
                        
                elif other_brand == 'Dodge':
                        button1 = st.sidebar.radio('Dodge', ['Avenger','Caliber','Caravan','Challenger','Charger','Dakota','Durango','Grand caravan','Intrepid', 
                                                             'Journey','Magnum','Neon','Nitro','Ram','Spirit','Stealth','Stratus','Viper','Voyager'])
                        
                elif other_brand == 'Dongben':
                        button1 = st.sidebar.radio('Dongben', ['DB X30','DB1021','SRM T20','SRM X30']) 
                        
                elif other_brand == 'Dongfeng':
                        button1 = st.sidebar.radio('Dongfeng', ['Fengxing CM7','Forthing T5','Future','Glory','Joyear S50','Joyear T5','Joyear X5','Lingzhi M3','SX6'])
                        
                elif other_brand == 'Ferrari':
                        button1 = st.sidebar.radio('Ferrari', ['488','SF90 Stradale','F12','Roma','F8','California','360 Modena','456','458','550','575','612','812', 
                                                               'Barchetta','Enze','F 355','F 360','F 430','F 50','F 512','GTC4Lusso','Maranello','Mondial','Monza','Portofino','Testarossa'])
                        
                elif other_brand == 'Fiat':
                        button1 = st.sidebar.radio('Fiat', ['500','Siena','Albea','Doblo','Seicento','Strada','126','Bachetta','Brava','Bravo','Cinquecento','Coupe','Croma','Ducato', 
                                                            'Duna','Fiorino','Idea','Marea','Marengo','Multipla','Panda','Pario','Punto','Regata','Ritmo','Scudo','Stilo','Talento', 
                                                            'Tempra','Tipo','Ulysse','Uno','X1/9'])                                  
                
                elif other_brand == 'GMC':
                        button1 = st.sidebar.radio('GMC', ['Envoy','Hummer','Jimmy','Savana','Sierra','Sonuna','Tracker','Yukon'])
                        
                elif other_brand == 'Haima':
                        button1 = st.sidebar.radio('Haima', ['2','3','Freema','7','Fstar','M3','M8','S5','S7','V70'])
                        
                elif other_brand == 'Haval':
                        button1 = st.sidebar.radio('Haval', ['H6'])  
                        
                elif other_brand == 'Hino':
                        button1 = st.sidebar.radio('Hino', ['500 Series','300 Series','700 Series'])   
                        
                elif other_brand == 'Hongqi':
                        button1 = st.sidebar.radio('Hongqi', ['E-HS9','H9'])    

                elif other_brand == 'Hummer':
                        button1 = st.sidebar.radio('Hummer', ['H1','H2','H3'])

                elif other_brand == 'Infiniti':
                        button1 = st.sidebar.radio('Infiniti', ['QX','EX','Q45','G37','FX','G20','G35','I20','I35','J30','JX','M30','Q30'])
                        
                elif other_brand == 'Jaguar':
                        button1 = st.sidebar.radio('Jaguar', ['XJ series','F-Pace','XF','F Type','XE','E Type','E-Pace','I-Pace','S Type','Sovereign','X Type','XK series'])    
                        
                elif other_brand == 'JRD':
                        button1 = st.sidebar.radio('JRD', ['Daily','Manjia','Mega','Travel'])            

                elif other_brand == 'Lamborghini':
                        button1 = st.sidebar.radio('Lamborghini', ['Urus','Huracan','Aventador','Diablo','Gallado','Murcielago'])
                        
                elif other_brand == 'Lifan':
                        button1 = st.sidebar.radio('Lifan', ['320','520','620']) 
                        
                elif other_brand == 'Lincoln':
                        button1 = st.sidebar.radio('Lincoln', ['Navigator','Aviator','Continental','Town car','Corsair','Nautilus','Blackwood','LX','Mart VIII','MKC','MKZ'])                                                                                                                   

                elif other_brand == 'Luxgen':
                        button1 = st.sidebar.radio('Luxgen', ['5','7 MPV','7 SUV','M7','S3','S5','U6','U7'])

                elif other_brand == 'Maserati':
                        button1 = st.sidebar.radio('Maserati', ['Levante','Ghibli','Quattroporte','MC20','GranTurismo','GranCabrio','3200GT','Biturbo','Gransport','Grecale','Spyder'])
                        
                elif other_brand == 'Maybach':
                        button1 = st.sidebar.radio('Maybach', ['57', '62'])
                        
                elif other_brand == 'McLaren':
                        button1 = st.sidebar.radio('McLaren', ['650s','720S','765LT','570S','12C','540C','570GT','600LT','675LT','F1','M6GT','P1','Senna','speedtail']) 
                        
                elif other_brand == 'Mekong':
                        button1 = st.sidebar.radio('Mekong', ['Paso','Premio','Pronto','Star'])                                                       

                elif other_brand == 'Morgan':
                        button1 = st.sidebar.radio('Morgan', ['Plus Four', 'Plus Six']) 
                
                elif other_brand == 'RAM':
                        button1 = st.sidebar.radio('RAM', ['1500','2500','3500'])
                
                elif other_brand == 'Renault':
                        button1 = st.sidebar.radio('Renault', ['Kaptur','21','Duster','Clio','Latitude','Koleos','11','19','25','4','9','Arkana','Avantime','Espace', 
                                                               'Express','Fluence','Grand Espace','Kangoo','Laguna','Logan','Magnum','Master','Megane','Modus','Rapid', 
                                                               'Safrane','Sandero','Scenic','Sport Spider','Super 5','Symbol','Talisman','Thalia','Trafic','Twingo','Vel satis','Wind'])
                        
                elif other_brand == 'Rolls Royce':
                        button1 = st.sidebar.radio('Rolls Royce', ['Ghost','Cullinan','Phantom','Silver','Corniche','Park ward','Dawn','Wraith']) 
                        
                elif other_brand == 'Samsung':
                        button1 = st.sidebar.radio('Samsung', ['QM5','SM3','SM5','SM7']) 
                        
                elif other_brand == 'Scion':
                        button1 = st.sidebar.radio('Scion', ['FR-S','Tc','Xb','Xd'])                                      

                elif other_brand == 'Skoda':
                        button1 = st.sidebar.radio('Skoda', ['Enyaq iV','Fabia','Kamiq','Karoq','Kodiaq','Octavia','Scala','Superb'])                                                                        

                elif other_brand == 'Smart':
                        button1 = st.sidebar.radio('Smart', ['City','Coupe','Crossblade','Forfour','Fortwo','MCC','Roadster'])

                elif other_brand == 'Ssangyong':
                        button1 = st.sidebar.radio('Ssangyong', ['Tivoli','Korando','Musso','Rexton','Stavic','Korando Sport','Actyon','Chairman','Family','Istana','Kalista','Kyron','XLV'])
                        
                elif other_brand == 'SYM':
                        button1 = st.sidebar.radio('SYM', ['T1000','T880','V11','V5'])                        

                elif other_brand == 'Thaco':
                        button1 = st.sidebar.radio('Thaco', ['Towner','Frontier','Ollin','Forland','Foton','Auman','Aumark','Mobihome','Town'])

                elif other_brand == 'Tobe':
                        button1 = st.sidebar.radio('Tobe', ['Mcar'])                        

                elif other_brand == 'UAZ':
                        button1 = st.sidebar.radio('UAZ', ['Hunter','Patriot','Pickup','Simbir'])

                elif other_brand == 'Vinaxuki':
                        button1 = st.sidebar.radio('Vinaxuki', ['1240T','Jinbei','1200B','Hafei','5500TL','990T','1490T','1980T','1990BA','2500BA', 
                                                                '3000BA','3450T','3500TL','3500TL','4500BA','4500BABD','5000BA','7000BA','8500TL'])

                elif other_brand == 'Wuling':
                        button1 = st.sidebar.radio('Wuling', ['Brilliance','Brilliance Van','Hongguang','Hongguang MiniEV','Sunshine'])

                elif other_brand == 'Zotye':
                        button1 = st.sidebar.radio('Zotye', ['Z8','T600','T300','Z100','Z300','Z500','Hunter'])
                        
                else:
                        url1 = 'https://bonbanh.com/oto/hang_khac'
                
        elif tag_brand == 'Audi':
                button1 = st.sidebar.radio('Audi', ['Q5','Q7', 'A6', 'A4', 'A8', 'A5', 'Q8', 'Q2', 'A7', '100', '200',
                                                        '80', '90', 'A1', 'A2', 'A3', 'Cabriolet', 'Coupe', 'E-tron',
                                                        'E-tron GT','Q3','Quattro','R8','RS2','RS4', 'S5','S8','TT','V8'])
                
        elif tag_brand == 'Bentley':
                button1 = st.sidebar.radio('Bentley', ['Flying Spur', 'Mulsanne', 'Bentayga', 'Continental', 'Arnage',
                                                'Azure', 'Brooklands', 'Turbo'])
                                        
        elif tag_brand == 'BMW':
                button1 = st.sidebar.radio('BMW', ['3 Series', '5 Series', '7 Series', 'X3', 'X6', 'X5', '4 Series', 
                                                        'X7', 'Z4', '1 Series', '2 Series', '6 Series', '8 Series', 'Alpina',
                                                        'i3', 'i8', 'iX', 'iX3', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M8', 'X1',
                                                        'X2', 'X4', 'XM', 'Z3', 'Z8'])               
                
        elif tag_brand == 'Chevrolet':
                button1 = st.sidebar.radio('Chevrolet', ['Spark', 'Cruze', 'Captiva', 'Colorado', 'Aveo', 'Trailblazer', 
                                                                'Vivant', 'Orlando', 'Camaro', 'Trax', 'Lacetti', 'Alero', 'Astro', 
                                                                'Avanlanche', 'Beretta', 'Caprice', 'Cavalier', 'Chevyvan' ,'Cobalt',
                                                                'Corsica', 'Corvette', 'Equinox', 'Explorer', 'Express', 'Impala',
                                                                'Ipanema', 'Kalos', 'Lumina', 'Malibu', 'Matiz', 'Nubira', 'Prizm',
                                                                'S 10', 'Silverado', 'Spectrum', 'SSR', 'Suburban', 'Tahoe', 'Tracker',
                                                                'Trans Sport', 'Venture'])
                
        elif tag_brand == 'Daewoo':
                button1 = st.sidebar.radio('Daewoo', ['Lacetti', 'Matiz', 'Gentra', 'Lanos', 'Nubira', 'Magnus', 'GentraX',
                                                        'Damas', 'Aranos', 'Arcadia', 'Brougham', 'Chairman', 'Cielo', 'Espero',
                                                        'Evanda', 'Istana', 'Kalos', 'Korando', 'Labo', 'Leganza', 'Lublin',
                                                        'Musso', 'Nexia', 'Novus', 'Polonez', 'Prince', 'Racer', 'Rexton',
                                                        'Rezzo', 'Statesman', 'Super Saloon', 'Tacuma', 'Tico', 'Tosca', 'Winstorm'])
                
        elif tag_brand == 'Ford':
                button1 = st.sidebar.radio('Ford', ['Ranger', 'Everest', 'Territory', 'EcoSport', 'Transit', 'Focus', 
                                                        'Fiesta', 'Escape', 'Explorer', 'Tourneo', 'Acononline', 'Aerostar', 
                                                        'Aspire', 'Bronco', 'Capri', 'Caravan', 'Cargo', 'Club wagon', 'Contour',
                                                        'Courier', 'Crown victoria', 'E450', 'Edge', 'Escort', 'EscurSeon',
                                                        'Expedition', 'Express', 'F150', 'F250', 'F350', 'F450', 'F700', 'Flex',
                                                        'Focus C Max', 'Fusion', 'Galaxie', 'Imax', 'Ka', 'Laser', 'Maverick',
                                                        'Mondeo', 'Mustang', 'Orion', 'Pinto', 'Probe', 'Puma', 'Sierra', 'Streetka',
                                                        'Taurus', 'Tempo', 'Windstar'])
                  
        elif tag_brand == 'Honda':
                button1 = st.sidebar.radio('Honda', ['CRV', 'City', 'Civic', 'HRV', 'Brio', 'BR V', 'Accord', 'Jazz',
                                                        'Odyssey', 'Capa', 'Concerto', 'CR X', 'CR Z', 'Domani', 'Element',
                                                        'FIT', 'FR V', 'Insight', 'Inspire', 'Integra', 'Legend', 'Life',
                                                        'Mobilo', 'NSX', 'Passport', 'Pilot', 'Prelude', 'S2000', 'Saber',
                                                        'Shuttle', 'Stream', 'Today', 'Torneo', 'Vigor', 'Z'])
                                
        elif tag_brand == 'Hyundai':
                button1 = st.sidebar.radio('Hyundai', ['Custin','Palisade','i10','SantaFe','Accent','Tucson','Elantra', 
                                                        'Kona','Creta','Getz','Stargazer','Avante','Atos','Azera','Centennial','Click', 
                                                        'County','Coupe','Custo','Dynasty','eMighty','Eon','Equus','Excel','Galloper', 
                                                        'Genesis','Gold','Grace','Grand Starex','Grandeur','H 1','H 100','H350','HD','i20', 
                                                        'i30','i40','Innovation','Ioniq 5','Lantra','Lavita','Libero','Marcia', 
                                                        'Matrix','Maxcruz','Mighty','Pony','Porter','S coupe','Santa Cruz','Santamo','Solati', 
                                                        'Sonata','Starex','Terracan','Tiburon','Trajet','Tuscani','Universe','Universe Xpress Luxury', 
                                                        'Veloster','Veracruz','Verna','Xcent','XG'])
                          
        elif tag_brand == 'Isuzu':
                button1 = st.sidebar.radio('Isuzu', ['Dmax','MU-X','QKR','Hi lander','NQR','NPR','Amigo','Ascender','Aska', 
                                                        'AXiom','Campo','D Cargo','Faster','FVR','Gemini','Midi','MU','NLR','NMR', 
                                                        'Panther','Pick up','Rodeo','Trooper','Turkuaz','Vehi cross','Wi zard'])
                   
        elif tag_brand == 'Jeep':
                button1 = st.sidebar.radio('Jeep', ['Wrangler','Gladiator','A2','Cherokee','Grand cherokee','Liberty','CJ',
                                                        'Compass','Grand Wagoneer'])
                                                
        elif tag_brand == 'Kia':
                button1 = st.sidebar.radio('Kia', ['Morning','Cerato','Carnival','K3','Sorento','Seltos','Sedona','Rio', 
                                                        'Carens','Soluto','Sonet','Forte','Avella','Bongo','Cadenza','Clarus','Concord', 
                                                        'Credos','Elan','Enterprise','Frontier','Jeep','Joice','K2700','K3000S','K4','K5', 
                                                        'K7','Lotze','Magentis','Opirus','Optima','Picanto','Potentia','Pregio','Pride',
                                                        'Quoris','Ray','Retona','Roadster','Rondo','Sephia','Shuma','Soul','Spectra', 
                                                        'Sportage','Visto','X Trek'])
                                                
                         
        elif tag_brand == 'LandRover':
                button1 = st.sidebar.radio('LandRover', ['Range Rover','Range Rover Evoque','Range Rover Sport', 
                                                                'Range Rover Velar','Defender','Discovery Sport','Discovery', 
                                                                'Freelander'])
                                                
        elif tag_brand == 'Lexus':
                button1 = st.sidebar.radio('Lexus', ['LX','RX','ES','GX','LS','NX','IS','GS','CT','HS','LC','LM','RC','SC','SL'])
                                                
                
                
        elif tag_brand == 'Mazda':
                button1 = st.sidebar.radio('Mazda', ['3','CX5','6','2','BT50','CX8','cx3','CX 30','323','626','121','323F',
                                                        '5','929','Atenza','AZ','B series','Bongo Friendee','Carol','Cronos','CX7', 
                                                        'CX9','Eunos','Familia','Millenia','MPV','MX 3','MX 5','MX 6','Pickup','Premacy', 
                                                        'RX 7','RX 8','Tribute','Xedos 9'])
                                                
        elif tag_brand == 'Mercedes Benz':
                button1 = st.sidebar.radio('Mercedes Benz', ['GLC','C class','E class','S class','Maybach','G class','GLS', 
                                                                'GLE Class','GLB','190','A class','AMG GT','Atego','B class', 
                                                                'CL class','CLA class','CLK class','CLS class','EQB','EQE','EQS', 
                                                                'GL','GLA class','GLK Class','M class','MB','ML Class','R class', 
                                                                'SL class','SLC','SLK class','SLR Mclaren','Sprinter','SR class', 
                                                                'V class','Vaneo','Viano','Vito'])
                          
        elif tag_brand == 'MG':
                button1 = st.sidebar.radio('MG', ['5','ZS','HS','X','ZT','MGF','3','350C','6','Express','RX5'])
                                                
        elif tag_brand == 'Mini':
                button1 = st.sidebar.radio('Mini', ['Cooper','One'])
             
        elif tag_brand == 'Mitsubishi':
                button1 = st.sidebar.radio('Mitsubishi', ['Xpander','Triton','Attrage','Outlander','Pajero Sport','Pajero', 
                                                                'Jolie','Mirage','Grandis','Lancer','Zinger','Outlander Sport','3000GT', 
                                                                'Airtek','Canter','Carisma','Challenger','Chariot','Colt','Delica', 
                                                                'Diamante','Dion','Eclipse','EK wagon','FTO','Galant','Grunder','GTO', 
                                                                'Hover','IO','Jeep','L200','L300','L400','Libero','Minica','Montero', 
                                                                'Pinin','Santamo','Savrin','Sigma','Space Gear','Space wagon','Starion', 
                                                                'Veryca','Xforce'])
                
        elif tag_brand == 'Nissan':
                button1 = st.sidebar.radio('Nissan', ['Navara','X trail','Almera','Sunny','Teana','Terra','Kicks','Grand livina', 
                                                        'Bluebird','Murano','Maxima','Qashqai','100NX','200SX','240SX','300ZX','350Z', 
                                                        '370Z','Altima','Armada','Avenir','Bassara','Cedric','Cefiro','Cima','Elgrand', 
                                                        'Frontier','Gloria','GT R','Juke','Langley','Largo','Laurel','Leaf','Liberty', 
                                                        'Livina','Micra','Moco','NV','Pathfinder','Patrol','Pick up','Pixo','Prairie', 
                                                        'Presage','Presea','President','Primastar','Primera','Pulsar','Quest','Rasheen', 
                                                        'Rogue','Safari','Sentra','Serena','Silvia','Skyline','Stagea','Stanza','Terrano', 
                                                        'Tiida','Tino','Urvan','Vanette','Versa','Wingroad','X Terra'])
                
        elif tag_brand == 'Peugeot':
                button1 = st.sidebar.radio('Peugeot', ['3008','2008','5008','408','Traveller','208','107','205','206', 
                                                                '207','305','306','307','308','309','404','405','406','407','504', 
                                                                '505','508','605','607','807','Boxer','J5','RCZ'])

        elif tag_brand == 'Porsche':
                button1 = st.sidebar.radio('Porsche', ['Cayenne','Panamera','Macan','718','911','Taycan','928','944', 
                                                                '968','Boxster','Carrera','Cayman'])
                        
        elif tag_brand == 'Subaru':
                button1 = st.sidebar.radio('Subaru', ['Forester','Outback','BRZ','WRX','Tutto','Levorg','Dex','Impreza', 
                                                        'Legacy','Tribeca','XV'])
           
        elif tag_brand == 'Suzuki':
                button1 = st.sidebar.radio('Suzuki', ['Swift','XL7','Super Carry Van','Ertiga','Super Carry Truck','Carry','Aerio', 
                                                        'Alto','APV','Baleno','Celerio','Ciaz','Cultis wagon','Esteem','Every landy', 
                                                        'Grand vitara','Jimmy','Kei','Liana','Samurai','SJ','SX4','Twin','Vitara','Wagon R+','X90'])
                    
        elif tag_brand == 'Toyota':
                button1 = st.sidebar.radio('Toyota', ['Vios','Fortuner','Innova','Camry','Corolla altis','Corolla Cross','Land Cruiser','Yaris','Prado','Veloz', 
                                                        'Wigo','Hilux','Raize','Sienna','4 Runner','86','Allion','Alphard','Altezza','Aristo','Aurion','Avalon','Avanza', 
                                                        'Avensis','Aygo','Blizzard','Brevis','C-HR','Caldina','Cami','Carina','Celica','Century','Chaser','Corolla','Corolla verso', 
                                                        'Corona','Corsa','Cressida','Cresta','Crown','Cynos','Estima','Fj cruiser','Gaia','Granvia','Harrier','Hiace','Highlander', 
                                                        'Ipsum','IQ','Liteace','Mark II','Matrix','Mega cruiser','MR 2','Picnic','Platz','Premio','Previa','Prius','Progres','Pronard','Raum', 
                                                        'RAV4','Rush','Scepter','Sequoia','Sera','Soarer','Solara','Starlet','Supra','Tacoma','Tercel','Townace','Tundra','Van','Venza','Verossa',
                                                        'Verso','Vista','Windom','Wish','XA','Yaris Cross','Yaris Verso','Zace'])
                
        elif tag_brand == 'VinFast':
                button1 = st.sidebar.radio('VinFast', ['Fadil','Lux A 2.0','Lux SA 2.0','VF8','VF5','VF9','VF e34','President','VF3','VF6','VF7'])                        
                
        elif tag_brand == 'Volkswagen':
                button1 = st.sidebar.radio('Volkswagen', ['Teramont','Tiguan','Touareg','Polo','T-Cross','Virtus','Beetle','Bora','Caddy','California','Corrado', 
                                                                'Crafter','Derby','Eos','Golf','Golf Plus','Jetta','Multivan','New Beetle','Passat','Phaeton','Routan',
                                                                'Scirocco','Sharan','Solo','Transporter','Vento','Viloran'])
                 
        elif tag_brand == 'Volvo':
                button1 = st.sidebar.radio('Volvo', ['XC90','XC60','S90','XC40','V60','S60','264','340 360','460','740','760','850','940','960','C70','S40', 
                                                        'Torslanda','V70','V90','XC70'])
                     
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