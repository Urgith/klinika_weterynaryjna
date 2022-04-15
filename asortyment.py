from sqlalchemy import create_engine
from datetime import date
# Wszystkie ceny w zł

produkty = ['preparat dyzenfykcyjny 5kg', 'preparat na rany', 'płyn do sporządzania roztworów do mycia 5l', 'test na badanie boreliozy',
                'obcinacz do pazurów dla kotów', 'obcinacz do pazurów dla psów', 'zestaw do pobierania moczu',
                'bandaż', 'termometr weteranyjny', 'kołnież ochronny', 'kompres gazowy', 'aplikator tabletek',
                'igła', 'strzykawka', 'maszynka do golenia', 'podkład chłonny', 'plaster tkaninowy', 'skalpel',
                'płyn do higienicznej i chirurgicznej dezynfekcji rąk', 'kompres żelowy', 'zestaw do bezpiecznego usuwania kleszczy',
                'zestaw do strzyżenia', 'żel do USG'
]

cena = [551, 96, 143, 110, 60, 100, 105, 80, 56, 360, 90, 40, 33, 81, 18, 43, 70, 64, 51, 35, 96, 78, 145, 12]
ilosc = [1, 6, 1, 10, 4, 4, 7, 10, 2, 30, 30, 5, 300, 300, 20, 30, 10, 20, 2, 5, 3, 3, 1, 1]
daty_produkty = [date(2021, 1, 1)]

produkty1 = ['preparat na rany', 'test na badanie boreliozy', 'zestaw do pobierania moczu', 'bandaż', 'kompres gazowy', 'igła', 'strzykawka',
                'maszynka do golenia', 'podkład chłonny', 'plaster tkaninowy 5m', 'skalpel', 'płyn do higienicznej i chirurgicznej dezynfekcji',
                'płyn do dezynfekcji powierzchni', 'leki na odrabaczanie', 'szczepionka na wściekliznę', 'igły do znieczuleń', 'testy alergiczne',
                'zestaw do czipowania', 'cewnik do inseminacji'
]

cena1 = [96, 110, 150, 80, 90, 33, 81, 18, 43, 35, 64, 51, 78, 60, 200, 35, 800, 100, 150]
ilosc1 = [6, 10, 10, 10, 30, 300, 300, 20, 30, 5, 20, 2, 3, 3, 10, 100, 10, 10, 10]
daty_produkty1 = [date(2021, 2, 1), date(2021, 3, 1), date(2021, 4, 1), date(2021, 5, 1), date(2021, 6, 1)]
#Produkty zamawiane co 3 miesiące
produkty3 = ['preparat do dezynfekcji 5kg', 'płyn do sporządzania roztworów do mycia 5l', 'termometr weteranyjny', 'kołnież ochronny',
                'aplikator tabletek', 'zestaw do bezpiecznego usuwania kleszczy', 'żel do USG'
]

ilosc3 = [1, 1, 2, 30, 5, 3, 1]
cena3 = [551, 143, 56, 360, 40, 96, 12]
daty_produkty3 = [date(2021, 4, 1)]
# meble, wyposażenie kliniki
meble_sprzet = ['stolik do instrumentów chirurgicznych', 'taboret', 'krzesło do poczekalni', 'chłodziarka medyczna','lampa medyczna',
                'stół weterynaryjny', 'wózek medyczny', 'szafka na leki i opatrunki', 'szafa kartotekowa', 'aparat do sztucznego oddychana',
                'skaler ultradźwiękowy','komputer','klawiatura','myszka','monitor','fotel biurowy',
                'biurko narożne', 'biurko'
]

meble_sprzet_cena = [1214, 320, 450, 2374, 1800, 2250, 300, 650, 1936, 250, 200, 4000, 200, 200, 1600, 800, 300, 300]
meble_sprzet_ilosc = [1, 1, 3, 1, 1, 1, 1, 5, 1, 1, 1, 4, 4, 4, 4, 4, 1, 3]
daty_meble_sprzet = [date(2021, 1, 1)]

commend = 'INSERT INTO asortyment(data_zakupu, cena, ilosc, produkt) VALUES '
for i in range(len(produkty)):
    commend += '({}, {}, {}, {}),'.format("'" + str(date(2021, 1, 1)) + "'", cena[i], ilosc[i], "'" + produkty[i] + "'")

for j in range(len(daty_produkty1)):
    for i in range(len(produkty1)):        
        commend += '({}, {}, {}, {}),'.format("'" + str(daty_produkty1[j]) + "'", cena1[i], ilosc1[i], "'" + produkty1[i] + "'")

for i in range(len(produkty3)):  
    commend += '({}, {}, {}, {}),'.format("'" + str(daty_produkty3[0]) + "'", cena3[i], ilosc3[i], "'" + produkty3[i] + "'")

for i in range(len(meble_sprzet)):
    commend += '({}, {}, {}, {}),'.format("'" + str(daty_meble_sprzet[0]) + "'", meble_sprzet_cena[i], meble_sprzet_ilosc[i], "'" + meble_sprzet[i] + "'")

engine = create_engine('mysql+pymysql://root:urgith@localhost:3306/klinika_weterynaryjna')
with engine.connect() as connection:
    connection.execute(commend[:-1])
