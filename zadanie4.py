

def zad1():
    uzytkownicy = {}
    login = input('wprowadz login: ')

    if len(login) > 5:
        True
    else:
        raise ValueError('login musi miec conajmniej 5 znakow')
    haslo = input('wprowadz haslo ')
    haslo2 = input('wprowadz haslo jescze raz ')
    if haslo == haslo2 and len(haslo) > 6:
        print('zalogowano pomyslnie')
        uzytkownicy[login] = haslo
    else:
        raise ValueError('wprowadzony login nie zgadza sie z pierwotnym, lub haslo nie ma 6 znakow')

    print(uzytkownicy)
zad1()



lista1 = [1, 2, 3]
def zad2(list1):
    v =0
    if len(list1) == 0:
        raise ValueError('lista nie moze byc pusta')
    else:
        pass
    while v < len(list1):
        if not type(list1[v]) == int and not type(list1[v]) == float:
            raise ValueError('lista musi zawierac wartosc typu "int"')
        v = v + 1

    return sum(list1), max(list1), min(list1)
print(zad2(lista1))





def zadanie3():
    uzytkownicy = {}

    while True:
        option = int(input('Podaj wybraną opcje: '))

        if option == 1:
            login = input('Podaj login: ')
            password = input('Podaj hasło: ')
            uzytkownicy[login] = password
            pass
        elif option == 2:
            for i in uzytkownicy:
                print(i, uzytkownicy[i])
            pass
        elif option ==3:
            nowe_haslo = input('wprowadz nowe haslo')
            uzytkownicy[login]= nowe_haslo
            print(uzytkownicy)
            return uzytkownicy.get(nowe_haslo)
            pass
        elif option == 4:
            nowy_login = input('prosze wpisac nowy login:')
            if nowy_login == login:
                uzytkownicy.clear()
            else:
                print('taki uzytkownik nie istnieje')
            pass
        elif option == 5:
            break



zadanie3()


