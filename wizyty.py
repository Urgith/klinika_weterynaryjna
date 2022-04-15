from sqlalchemy import create_engine
from datetime import timedelta
from datetime import datetime
import numpy as np


engine = create_engine('mysql+pymysql://root:urgith@localhost:3306/klinika_weterynaryjna')

rejestracje = []
wylosowana = datetime(2021, 1, 1)
while wylosowana < datetime(2021, 7, 1):
    wylosowana += timedelta(minutes=int(np.random.exponential(scale=30)))

    if wylosowana.weekday() != 6 and 10 <= wylosowana.hour <= 17:
        rejestracje.append(wylosowana)
##########

with engine.connect() as connection:
    zwierze_wlasciciel_rejestracja = connection.execute('SELECT zwierzeta.id_zwierzecia, wlasciciele.id_wlasciciela, data_rejestracji FROM wlasciciele INNER JOIN zwierzeta ON wlasciciele.id_wlasciciela=zwierzeta.id_wlasciciela').fetchall()
##########

zwierze_wlasciciel_rejestracja_termin = []
for zwierze in zwierze_wlasciciel_rejestracja:
    for rejestracja in rejestracje:
        if zwierze[2] < rejestracja:
            zwierze_wlasciciel_rejestracja_termin.append(list(zwierze) + [rejestracja])
            rejestracje.remove(rejestracja)
            break
##########

liczba_zwierzat = len(zwierze_wlasciciel_rejestracja_termin)
for rejestracja in rejestracje:

    wylosowane = np.random.randint(0, liczba_zwierzat)
    if zwierze_wlasciciel_rejestracja_termin[wylosowane][2] < rejestracja:
        zwierze_wlasciciel_rejestracja_termin.append(zwierze_wlasciciel_rejestracja_termin[wylosowane][:-1] + [rejestracja])
##########

zwierze_termin = []
for element in zwierze_wlasciciel_rejestracja_termin:
    zwierze_termin.append([element[0], element[3]])

zwierze_termin = sorted(zwierze_termin, key=lambda termin: termin[1])
##########

mozliwe_zabiegi = [list(range(1, 38)) for i in range(liczba_zwierzat)]
martwe = []
for zwierze in zwierze_termin:
    if zwierze[0] in martwe:
        continue

    wylosowana = np.random.choice(mozliwe_zabiegi[zwierze[0] - 1])
    if wylosowana in [2, 3, 12, 13]:
        mozliwe_zabiegi[zwierze[0] - 1].remove(wylosowana)
    elif wylosowana == 6:
        martwe.append(zwierze[0])

    zwierze.append(wylosowana)
##########

wizyty = []
wizyta = datetime(2021, 1, 1)
while wizyta < datetime(2021, 7, 1):
    wizyta += timedelta(minutes=30)

    if wizyta.weekday() != 6 and 10 <= wizyta.hour <= 17:
        wizyty.append(wizyta)

przeskok = 0
for i in range(len(zwierze_termin)):
    for j in range(i + przeskok, len(wizyty)):
        if zwierze_termin[i][1] < wizyty[j]:
            zwierze_termin[i] += [wizyty[j]]
            break

        przeskok += 1

zwierze_termin = [element for element in zwierze_termin if len(element) == 4]
##########

przedzial1 = (datetime(2021, 6, 30) - datetime(2021, 1, 1)).days
przedzial2 = (datetime(2021, 6, 30) - datetime(2021, 4, 1)).days

dni_bez_asystenta1 = list(set([datetime(2021, 1, 1).date() + timedelta(days=np.random.randint(0, przedzial1 + 1)) for i in range(np.random.randint(1, 8))]))
dni_bez_asystenta2 = list(set([datetime(2021, 4, 1).date() + timedelta(days=np.random.randint(0, przedzial2 + 1)) for i in range(np.random.randint(1, 4))]))
dni_bez_lekarza = list(set([datetime(2021, 4, 1).date() + timedelta(days=np.random.randint(0, przedzial2 + 1)) for i in range(np.random.randint(1, 4))]))

dni_bez_obslugi1 = list(set([datetime(2021, 1, 1).date() + timedelta(days=np.random.randint(0, przedzial1 + 1)) for i in range(np.random.randint(1, 10))]))
dni_bez_obslugi2 = list(set([datetime(2021, 4, 1).date() + timedelta(days=np.random.randint(0, przedzial2 + 1)) for i in range(np.random.randint(1, 5))]))
##########

commend = 'INSERT INTO wizyty(id_zwierzecia, id_czynnosci, id_zmiany, data_rejestracji, data_wizyty) VALUES '
for element in zwierze_termin:
    data_r = element[1].date()
    data_w = element[3].date()
    zatrudnienie = datetime(2021, 4, 1).date()
    id_zmiany = 1

    if data_r <= zatrudnienie:
        if data_r in dni_bez_obslugi1:
            id_zmiany += 1
    elif element[1].hour <= 13:
        if data_r in dni_bez_obslugi1 and data_r in dni_bez_obslugi2:
            id_zmiany += 1
        elif data_r in dni_bez_obslugi1:
            id_zmiany += 2
    else:
        if data_r in dni_bez_obslugi1 and data_r in dni_bez_obslugi2:
            id_zmiany += 1
        elif data_r not in dni_bez_obslugi2:
            id_zmiany += 2

    if data_w <= zatrudnienie:
        if data_w not in dni_bez_asystenta1:
            id_zmiany += 3
    elif element[3].hour <= 13:
        if data_w in dni_bez_asystenta1 and data_w in dni_bez_asystenta2:
            pass
        elif data_w not in dni_bez_asystenta1:
            id_zmiany += 3
        elif data_w in dni_bez_asystenta1:
            id_zmiany += 6
    else:
        if data_w in dni_bez_asystenta1 and data_w in dni_bez_asystenta2:
            pass
        elif data_w in dni_bez_asystenta2:
            id_zmiany += 3
        elif data_w not in dni_bez_asystenta2:
            id_zmiany += 6

        if data_w not in dni_bez_lekarza:
            id_zmiany += 9

    commend += '({}, {}, {}, {}, {}),'.format(element[0], element[2], id_zmiany, "'" + str(element[1]) + "'", "'" + str(element[3]) + "'")

with engine.connect() as connection:
    connection.execute(commend[:-1])
