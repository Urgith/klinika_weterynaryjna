from sqlalchemy import create_engine
from dateutil.relativedelta import relativedelta
from datetime import datetime
import numpy as np


engine = create_engine('mysql+pymysql://root:urgith@localhost:3306/klinika_weterynaryjna')
result = engine.execute('SELECT id_pracownika, data_zatrudnienia, stanowisko_pracy FROM pracownicy')

id, zatrudnienie, stanowisko = [], [], []
for row in result:
    id.append(row['id_pracownika'])
    zatrudnienie.append(row['data_zatrudnienia'])
    stanowisko.append(row['stanowisko_pracy'])

result.close()

zarobki = {'lekarz weterynarii': (6000, 400), 'informatyk': (4500, 350), 'handlowiec': (4000, 300), 'technik weterynarii': (3500, 250), 'obsługa klienta': (2500, 200), 'woźny': (2500, 200)}
etaty = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],  [0, 0, 0], [0, 0, 0], [0, 0, 0]]
nazwy_etatow = {0:'pół', 1:'pełen'}

commend = 'INSERT INTO zarobki(id_pracownika, etat, wyplata, od, do, premia) VALUES '
for i in range(len(id)):
    start = zatrudnienie[i]
    wyplata = 0
    premia = 0
    j = 0
    etat = etaty[i][0]

    while start <= datetime(2021, 6, 30).date():
        if i != 0 and j==0:
            wyplata = np.round(np.random.normal(zarobki[stanowisko[i]][0], zarobki[stanowisko[i]][1]), 2) / (2 - etaty[i][j])

        if etaty[i][j] != etat:
            wyplata //= 2
            premia //= 2

            etat = etaty[i][j]

        commend += '({}, {}, {}, {}, {}, {}),'.format(id[i], "'" + nazwy_etatow[etaty[i][j]] + "'", wyplata, "'" + str(start) + "'", "'" + str(min(datetime.now().date(), start + relativedelta(months=1))) + "'", premia)
        start += relativedelta(months=1)

        if i != 0:
            premia += np.round(np.random.normal(zarobki[stanowisko[i]][0] / 100, zarobki[stanowisko[i]][1] / 10) / (2 - etaty[i][j]), 2)

        j += 1

with engine.connect() as connection:
    connection.execute(commend[:-1])
