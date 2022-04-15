from sqlalchemy import create_engine
import pandas as pd


engine = create_engine('mysql+pymysql://root:urgith@localhost:3306/klinika_weterynaryjna')
czynnosci = pd.read_csv('data/uslugi.csv', delimiter=';', header=None, names=['id_czynnosci', 'czynnosc', 'cena'])
czynnosci.to_sql('czynnosci', con=engine, if_exists='append', index=False)
