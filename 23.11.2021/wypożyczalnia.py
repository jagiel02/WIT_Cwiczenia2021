


is_authenticated = False
movies = {}
users = {}


def register_user():
    login = input('wprowadz login')
    haslo = input('wprowadz haslo')
    users[login] = haslo

def add_movie():
    nazwa = input('wprowadz nazwe flimu')
    ilosc = int(input('wprowadz ilosc dostepnosci filmu'))
    movies[nazwa] = ilosc
    pass

def modify_movie():
    nowa_ilosc= input('wprowadz nowa ilosc dla filmu: ')
    nowa_nazwa = int(input('wprowadz nazwe jeszcze raz'))
    movies.clear()
    return movies[nowa_nazwa] == nowa_ilosc


def get_movies():
    for key,values in movies.items():
        print(key, values)
    pass

def check_movie_availability():
    wprowadz = input('wprowadz nazwe filmu, aby sprawdzic jego dostepnosc')
    
    if wprowadz in movies:
        print('w bazie jest taki film')
    else:
        print('w bazie nie ma takiego filmu')
        

def rent_movie():
    wprowadz = input('wprowadz nazwe filmu, aby go wypozyczyc')

    if wprowadz in movies:
        print('wypozyczono')
        for i in movies.keys():
            movies[i] -=  1
        print(movies)
    else:
        print('nie mozna wypozyczyc')
    
    
def login_user():
    login = input('wprowadz login do logowania')
    haslo = input('wprowadz haslo do logowania')
    
    users[login] = haslo
    print(users)
    pass


if is_authenticated == False:
    while True:
        print('''
        nie zalogowany
    1). Zobacz całą ofertę
    2). Sprawdź dostępność filmu
    3). Zaloguj się
    0). Wyjdź z programu
            ''')
        a = int(input('wybierz opcje(0-7)'))
        if a == 1:
            get_movies()
        if a == 2:
            check_movie_availability()
        if a == 3:
            register_user()
            if len(users) >= 1:
                is_authenticated = True
            if is_authenticated == True:
                while True:
                    print('''
            zalogowany
    1). Utwórz użytkownika
    2). Dodaj film
    3). Zmodyfikuj ilość dostępnego filmu
    4). Zobacz całą ofertę
    5). Sprawdź dostępność filmu
    6). Wypożycz film
    7). Zaloguj się
    0). Wyjdź z programu
                ''')
                    b = int(input('wybierz opcje(0-7)'))


                    if b ==1:
                        register_user()
                    if b == 2:
                        add_movie()
                    if b ==3:
                        modify_movie()
                    if b == 4:
                        get_movies()
                        
                    if b ==5:
                        check_movie_availability()
                        
                    if b == 6:
                        rent_movie()
                        
                    if b == 7:
                        login_user()
                        

                    if b == 0:
                        break
        if a == 0:
            break




