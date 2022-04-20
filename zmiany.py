from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:urgith@localhost:3306/klinika_weterynaryjna')
result = engine.execute("SELECT id_pracownika, stanowisko_pracy FROM pracownicy WHERE stanowisko_pracy='lekarz weterynarii' OR stanowisko_pracy='technik weterynarii' OR stanowisko_pracy='obsługa klienta' OR stanowisko_pracy='informatyk'")

lekarze, rejestratorzy, asystenci = [], [], ['NULL']
for row in result:
    if row['stanowisko_pracy'] == 'lekarz weterynarii':
        lekarze.append(row['id_pracownika'])

    elif row['stanowisko_pracy'] == 'technik weterynarii':
        asystenci.append(row['id_pracownika'])

    else:
        rejestratorzy.append(row['id_pracownika'])

result.close()

commend = 'INSERT INTO zmiany(id_lekarza, id_asystenta, id_rejestratora) VALUES '
for l in lekarze:
    for a in asystenci:
        for r in rejestratorzy:
            commend += '({}, {}, {}),'.format(l, a, r)

with engine.connect() as connection:
    connection.execute(commend[:-1])
