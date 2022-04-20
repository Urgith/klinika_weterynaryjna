from sqlalchemy import create_engine
from datetime import timedelta
from datetime import datetime
import pandas as pd
import numpy as np


imiona_m = pd.read_csv('data/imiona_m.csv', delimiter=';', usecols=['IMIĘ_PIERWSZE', 'LICZBA_WYSTĄPIEŃ'])
imiona_k = pd.read_csv('data/imiona_k.csv', delimiter=';', usecols=['IMIĘ_PIERWSZE', 'LICZBA_WYSTĄPIEŃ'])
nazwiska_m = pd.read_csv('data/nazwiska_m.csv')
nazwiska_k = pd.read_csv('data/nazwiska_k.csv')
adres = pd.read_csv('data/adres.csv', usecols=['ETYKIETA_NAZWA_SKROCONA'])

commend = 'INSERT INTO wlasciciele(imie, nazwisko, telefon, adres, data_rejestracji) VALUES '
for i in range(400):
    start_klient = datetime(2021, 1, 1, 0, 0, 0)
    end_klient = datetime(2021, 6, 30, 17, 0, 0)
    random_klient = np.random.randint((end_klient - start_klient).total_seconds() // 60)

    data_rejestracji = start_klient + timedelta(minutes=random_klient)
    while data_rejestracji.weekday() == 6 or not(11 <= data_rejestracji.hour <= 16):
        random_klient = np.random.randint((end_klient - start_klient).total_seconds() // 60)
        data_rejestracji = start_klient + timedelta(minutes=random_klient)

    if np.random.random() < 0.5:
        plec = 'M'
    else:
        plec = 'K'

    if plec == 'M':
        commend += '({}, {}, {}, {}, {}),'.format("'" + imiona_m['IMIĘ_PIERWSZE'].sample(n=1, weights=imiona_m['LICZBA_WYSTĄPIEŃ']).values[0] + "'", "'" + str(nazwiska_m['Nawisko aktualne'].sample(n=1, weights=nazwiska_m['Liczba']).values[0]) + "'", str(int(534720811 + (154406493*np.random.random()))), "'" + adres['ETYKIETA_NAZWA_SKROCONA'].sample(n=1).values[0] + "'", "'" + str(data_rejestracji) + "'")

    else:
        commend += '({}, {}, {}, {}, {}),'.format("'" + imiona_k['IMIĘ_PIERWSZE'].sample(n=1, weights=imiona_k['LICZBA_WYSTĄPIEŃ']).values[0] + "'", "'" + str(nazwiska_k['Nawisko aktualne'].sample(n=1, weights=nazwiska_k['Liczba']).values[0]) + "'", str(int(534720811 + (154406493*np.random.random()))), "'" + adres['ETYKIETA_NAZWA_SKROCONA'].sample(n=1).values[0] + "'", "'" + str(data_rejestracji) + "'")

engine = create_engine('mysql+pymysql://root:urgith@localhost:3306/klinika_weterynaryjna')
with engine.connect() as connection:
    connection.execute(commend[:-1])          
