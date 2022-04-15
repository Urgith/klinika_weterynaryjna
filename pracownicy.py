from sqlalchemy import create_engine

from dateutil.relativedelta import relativedelta
from datetime import timedelta
from datetime import date

import pandas as pd
import numpy as np


imiona_m = pd.read_csv('imiona_m.csv', delimiter=';', usecols=['IMIĘ_PIERWSZE', 'LICZBA_WYSTĄPIEŃ'])
imiona_k = pd.read_csv('imiona_k.csv', delimiter=';', usecols=['IMIĘ_PIERWSZE', 'LICZBA_WYSTĄPIEŃ'])

nazwiska_m = pd.read_csv('nazwiska_m.csv')
nazwiska_k = pd.read_csv('nazwiska_k.csv')

ulice = pd.read_csv('adres.csv', usecols=['ETYKIETA_NAZWA_SKROCONA'])

s = ['lekarz weterynarii', 'technik weterynarii', 'obsługa klienta',
     'informatyk', 'handlowiec', 'woźny']

stanowiska_pracy = [s[0], s[1], s[2], s[3], s[4], s[5], s[0], s[1], s[2]]

commend = 'INSERT INTO pracownicy(imie, nazwisko, plec, data_urodzenia, adres_zamieszkania, numer_telefonu, stanowisko_pracy, data_zatrudnienia) VALUES '
for i in range(len(stanowiska_pracy)):
    start_ur = date(1970, 1, 1)
    end_ur = date(2000, 12, 31)
    random_ur = np.random.randint((end_ur - start_ur).days)

    start_zat = date(2021, 1, 1)

    if np.random.random() < 0.5:
        plec = 'mężczyzna'
    else:
        plec = 'kobieta'

    if plec == 'mężczyzna':
        commend += '({}, {}, {}, {}, {}, {}, {}, {}),'.format("'" + imiona_m['IMIĘ_PIERWSZE'].sample(n=1, weights=imiona_m['LICZBA_WYSTĄPIEŃ']).values[0] + "'", "'" + str(nazwiska_m['Nawisko aktualne'].sample(n=1, weights=nazwiska_m['Liczba']).values[0]) + "'", "'" + str(plec) + "'", "'" + str(start_ur + timedelta(days=random_ur)) + "'", "'" + str(ulice.sample().values[0, 0]) + "'", "'" + str(int(534720811 + 154406493*np.random.random())) + "'", "'" + stanowiska_pracy[i] + "'", "'" + str(str(start_zat + min(i//6, 1)*relativedelta(months=3))) + "'")

    else:
        commend += '({}, {}, {}, {}, {}, {}, {}, {}),'.format("'" + imiona_k['IMIĘ_PIERWSZE'].sample(n=1, weights=imiona_m['LICZBA_WYSTĄPIEŃ']).values[0] + "'", "'" + str(nazwiska_k['Nawisko aktualne'].sample(n=1, weights=nazwiska_k['Liczba']).values[0]) + "'", "'" + str(plec) + "'", "'" + str(start_ur + timedelta(days=random_ur)) + "'", "'" + str(ulice.sample().values[0, 0]) + "'", "'" + str(int(534720811 + 154406493*np.random.random())) + "'", "'" + stanowiska_pracy[i] + "'", "'" + str(str(start_zat + min(i//6, 1)*relativedelta(months=3))) + "'")

engine = create_engine('mysql+pymysql://root:urgith@localhost:3306/klinika_weterynaryjna')
with engine.connect() as connection:
    connection.execute(commend[:-1])
