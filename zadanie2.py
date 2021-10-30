#zad1

lista = [1, 2, 3, 4, 5]

odwrocona_lista = []
i = -1
while True:
    odwrocona_lista.append(lista[i])
    i = i -1
    if len(odwrocona_lista) == 5:
        break

print('odwrotna lista=', odwrocona_lista)

#zad2

lista.sort()
print('lista max= ',max(lista[:4]),',', max(lista[:5]))
#print('lista_max =', lista[3:])


#zad3

lista1=[]
i =1
for i in range(2,13):
    i = i+1
    lista1.append(i)
print('lista1 =',lista1)

lista2=[]

o = -1
while True:
    o = o + 1
    lista2.append(o)
    if len(lista2) == 12:
        break
print('lista2 =',lista2)


#zad4

dane_logowania = {
    "Admin" : "1234"
}

while True:
    nazwa = (input('wprowadz swoja nazwe uzytkownika: '))
    if dane_logowania.get(nazwa):
        print('pomyslne dane')
    else:
        print('zle dane')
        continue
    haslo = input('wpisz haslo: ')
    if dane_logowania.get(nazwa, haslo):
        print('poprawne haslo')
        break
    else:
        print('niepoprwane haslo')
        continue


#zad5

lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
lista3 = [1,2,2,3,3,4,5]


a = set(lista1 and lista2 and lista3)
print(a)


if len(set(lista1)) !=  len(set(lista2)) or len(set(lista3)):
    print('listy maja powtorki')
else:
    print ('ni ma powtorek')





















lista2=[]


