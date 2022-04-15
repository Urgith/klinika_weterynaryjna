from sqlalchemy import create_engine
import datetime
import random
import csv


names_M = []
names_K = []

fileM = open("data/imionaM.csv",encoding='utf8')
readM = csv.reader(fileM)

fileK = open("data/imionaK.csv",encoding='utf8')
readK = csv.reader(fileK)

for row in readM:
    names_M.append(row[0])
del names_M[0]

for row in readK:
    names_K.append(row[0])
del names_K[0]

species = ['Pies','Kot','Królik','Chomik','Mysz','Szczur']

dog_breed = ['Buldog amerykański','Alpejski gończy krótkonożny','Amerykański pitbulterier','Cocker spaniel amerykański',
            'Terier australijski','Bernardyn','Berneński pies pasterski','Buldog francuski','Wyżeł włoski krótkowłosy','Bulterier',
            'Pudel','Owczarek portugalski','Grzywacz chiński','Pies chodzki','Owczarek szkocki długowłosy','Owczarek szkocki krótkowłosy',
            'Jamnik','Dalmatyńczyk','Bokser','Owczarek niemiecki','Szpic niemiecki','Doberman','Dog argentyński','Gończy węgierski',
            'Wyżeł duński','Gończy polski','Owczarek kataloński','Owczarek kaukaski','Mastif angielski','Pekińczyk','Owczarek podhalański',
            'Samojed','Husky syberyjski']

cat_breed = ['Tonkijski','Syjamski','Sfinks','Rosyjski niebieski','Pixie-bob','Perski','Orientalny','Maine coon','Korat',
             'Himalayan','Japoński bobtail','Egipski mau','Doński sfinks','Chausie','Burmilla','Brytyjski krótkowłosy',
             'Brytyjski długowłosy','Birmański','Amerykański curl długowłosy']

rabbit_breed = ['Belgijski olbrzym','Francuski baran','Angielski baran','Kalifornijski','Popielański biały','Angora Biała','Mały baran']

mouse_breed = ['Krótkowłosa','Długowłosa','Loczkowana','Satynowa','Abisyńska']

chamster_breed = ['Syryjski','Chiński','Dżungarski','Zabajkalski']

rat_breed = ['Wędrowny','Śniady','Polinezyjski']

### wagi i wzrosty minimalne i maksymalne odpowiadają rasom psów znajdujących się na tych samych pozycjach w dog_breed ###

weight_min_dog = [32,15,14,8,4,55,40,8,25,10,13,12,4,16,18,18,5,22,25,25,15,35,40,30,25,22,16,50,75,3,45,25,18]

weight_max_dog = [68,18,27,13,7,100,60,14,40,18,28,18,6,25,25,25,8,26,30,55,28,45,45,35,35,26,18,80,100,6,60,30,27]

height_min_dog = [51,36,43,34,20,65,58,24,55,35,45,40,23,48,51,51,17,55,53,55,40,63,60,50,50,50,45,64,70,15,60,50,50]

height_max_dog = [71,38,53,40,25,90,70,35,67,45,60,48,33,56,61,61,25,61,63,65,55,73,68,55,60,60,55,78,90,20,70,60,56]

animals = []
breeds = []
sex_list = []
names = []
owners = []
birth_dates = []
weights = []
heights = []
ages = []

def random_date(start, end):
    delta = end - start
    int_delta = delta.days
    random_day = random.randrange(int_delta)
    return start + datetime.timedelta(days = random_day)

for i in range(400):
    owners.append(i+1)

for i in range(300):
    ow = random.randint(1, 400)
    owners.append(ow)

random.shuffle(owners)

for i in range(700):
    a = random.random()

    if 0.0 <= a <= 0.5:
        animal = species[0]
    elif 0.5 < a <= 0.8:
        animal = species[1]
    elif 0.8 < a <= 0.85:
        animal = species[2]
    elif 0.85 < a <= 0.9:
        animal = species[3]
    elif 0.9 < a <= 0.95:
        animal = species[4]
    else:
        animal = species[5]

    animals.append(animal)
    end_date = datetime.datetime.strptime('1/1/2021', '%m/%d/%Y').date()
    today = datetime.datetime.strptime('6/30/2021', '%m/%d/%Y').date()

    if animal == 'Pies':
        breed = random.sample(dog_breed,1)
        indeks = dog_breed.index(breed[0])

        w_min = weight_min_dog[indeks]
        w_max = weight_max_dog[indeks]
        h_min = height_min_dog[indeks]
        h_max = height_max_dog[indeks]

        weight = round(random.uniform(w_min,w_max),1)
        height = round(random.uniform(h_min,h_max),1)
        start = datetime.datetime.strptime('1/1/2008', '%m/%d/%Y').date()
        birth_date = random_date(start,end_date)

    elif animal == 'Kot':
        breed = random.sample(cat_breed,1)
        weight = round(random.uniform(3,8),1)
        height = round(random.uniform(20,33),1)
        start = datetime.datetime.strptime('1/1/2010', '%m/%d/%Y').date()
        birth_date = random_date(start,end_date)

    elif animal == 'Królik':
        breed = random.sample(rabbit_breed,1)
        weight = round(random.uniform(2,4),1)
        height = round(random.uniform(15,20),1)
        start = datetime.datetime.strptime('1/1/2018', '%m/%d/%Y').date()
        birth_date = random_date(start,end_date)

    elif animal == 'Chomik':
        breed = random.sample(chamster_breed,1)
        weight = round(random.uniform(0.1,0.3),2)
        height = round(random.uniform(4,7),1)
        start = datetime.datetime.strptime('1/1/2018', '%m/%d/%Y').date()
        birth_date = random_date(start,end_date)

    elif animal == 'Mysz':
        breed = random.sample(mouse_breed,1)
        weight = round(random.uniform(0.1,0.2),2)
        height = round(random.uniform(3,6),1)
        start = datetime.datetime.strptime('1/1/2018', '%m/%d/%Y').date()
        birth_date = random_date(start,end_date)

    else:
        breed = random.sample(rat_breed,1)
        weight = round(random.uniform(0.1,0.4),2)
        height = round(random.uniform(5,8),1)
        start = datetime.datetime.strptime('1/1/2018', '%m/%d/%Y').date()
        birth_date = random_date(start,end_date)

    breeds.append(breed[0])
    weights.append(weight)
    heights.append(height)
    birth_dates.append(birth_date)

    time_difference =  today - birth_date
    age = round((time_difference.days)/365,1)
    ages.append(age)

    b = random.random()

    if b <= 0.5:
        sex = 'samiec'
        name = random.sample(names_M,1)
    else:
        sex = 'samica'
        name = random.sample(names_K,1)

    sex_list.append(sex)
    names.append(name[0])

commend = 'INSERT INTO zwierzeta(id_wlasciciela, zwierze, rasa, plec, imie, data_urodzenia, wiek, waga, wzrost) VALUES '
for i in range(len(animals)):
    commend += '({}, {}, {}, {}, {}, {}, {}, {}, {}),'.format(owners[i], "'" + animals[i] + "'", "'" + breeds[i] + "'", "'" + sex_list[i] + "'", "'" + names[i] + "'", "'" + str(birth_dates[i]) + "'", ages[i], weights[i], heights[i])

engine = create_engine('mysql+pymysql://root:urgith@localhost:3306/klinika_weterynaryjna')
with engine.connect() as connection:
    connection.execute(commend[:-1])
