#Instrukcje warunkowe


def zad1():
    wiek = int(input('Podaj swój wiek: '))
    if wiek >= (18):
        print('Jesteś pełnoletni/-a')
    else:
        print ('Nie masz ukończonych 18 lat')


def zad2():
    wiek2 = int(input('Podaj swój wiek: '))
    if wiek2 > 18:
        print('Możesz prowadzić samochód oraz głosować w wyborach')
    elif wiek2 >= 17 and wiek2 <18:
        print ('Możesz prowadzić samochód')
    elif wiek2 < 17:
        print ('Nie możesz głosować ani prowadzić samochodu')



def zad3():
    #średnia prędkość pociągu 90km/h
    trasa = int(input('Wpisz z jaką średnią prędkością chciałbyś jechać samochodem: '))
    if trasa > 90:
        print('pokonasz tą odległość szybciej samochodem')
    else:
        print('ta trase pokonasz pociągiem szybciej')

def zad4():
    poczatkowy_kapital = int(input('Podaj swój początkowy kapitał: '))
    miesieczne_wplywy = int(input('Podaj swoje miesieczne wplywy:'))
    okres_inwestowania = int(input('Podaj swoj okres inwestowania: '))
    koncowa = int(input('ile chcialbys na koniec uzyskac pieniedzy?: '))


#Czesc 2


for i in range (0,10):
    print(i)

for i in range (10, 21):
    print(i)


for i in range (3, 19, 4):
    print(i)


x= 3
przerwa = 0

while x <= 20:
    if przerwa == 4:
        przerwa = 0
    if przerwa == 0:
        print(x)
    x = x+1
    przerwa = przerwa+1



count =0
while count < 10:
    print(count)
    count = count + 1


x = 10
while x < 21:
    print(x)
    x = x + 1

y = 3



for i in 'Warszawa':
    print(i)

miasto = 'Warszawa'
i = 0
while i < len(miasto):
    print(miasto[i])
    i += 1\



for i in range (10):
    for i in range(6):
        if i <6:
            print (i)



while True:
    username = (input('podaj dane: '))
    if username != 'Admin':
        continue
    else:
        password = int(input('podaj haslo'))
    if password != 1234:
        continue
    else:
        break



























