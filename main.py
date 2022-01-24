import random
import time
users = {}
podroze = []
fav_places = []
kontakty = []
miejsca = []

def register_user():
    login = input('wprowadz login')
    haslo = input('wprowadz haslo')
    users[login] = haslo 
    
    
class opcje_klienta:
    
    
    def trip_calculate():
        print('Cennik za 1km = 3zł')
        odleglosc =int(input('prosze wprowadzic odgległość (w km) jaka chesz pokonac: '))
        wynik = odleglosc * 3
        print('Cena za twój przejazd bedzie wynosic okolo: ', wynik, 'zł')
        
        
        
    def time_calculate():
        wynik = 0
        print('średni czas przejazdu (na 1km) wynosi około 2.5min ')
        odleglosc =int(input('prosze wprowadzic odgległość (w km) jaka chesz pokonac: '))
        wynik = odleglosc * 2.5
        print('Twój przejazd będzie trwać około: ', wynik, 'min')
    
    

            
    def start_journey():
        miejsce= input('Wpisz proszę swoj adres destynacji: ')
        if len(miejsce) > 0: 
                miejsca.append(miejsce)
                print('trwa potwierdzanie przejazdu do :', miejsca, '....')
                time.sleep(3)
                print('potwierdzono przejazd proszę sie spodziewać kierowcy')
                return podroze == True
                
    
        else:
            print('prosze wpisac adres podrozy') 
            return opcje_klienta.start_journey()
        
        
        
    def active_journeys():
        
        if len(miejsca) == 0:
            print('nie masz zadnych aktywnych podrozy')
        else:
            print('Masz aktywny przejazd do: ', miejsca)
        
        
        
        """
        if podroze == False:
            print('Nie masz aktualnie trwajacych przejazdow')
            
        else:
            print('Masz aktywny przejazd do: ', miejsca)
        """
        
    def his_trip():
        if len(miejsca) == 0:
            print('nie masz zadnych przejazdow')
        else:
            print('Odbyles podroz do: ', miejsca)
            
            
    def fav_places():
        fav = input('wpisz nazwe miejsca którego chcesz dodać do swoich ulubionych')
        
        if bool(fav) == False:
                print('nie wpisano nazwy')    
        else:
            fav_places.append(fav)
            print('Dodano: ',fav_places,'do listy ulubionych miejsc')
            
            
    def share_route():
        
        if len(miejsca) > 0:
            kontakt = input('wprowadz nazwe ')
            kontakty.append(kontakt)
            print('pomyslnie udostepniono trase: ', kontakt)
            
        else:
            print('nie odbywasz teraz zadnej podrozy')
            
        
    def logout():
        return register_user()
    

class Kierowca(opcje_klienta):
    
    def start_job():
        print('wyszukuje klientów w twojej okolicy....')
        time.sleep(3)
        print('znaleziono klienata ', random.randint(1,4), 'km od ciebie')
        miejsca.append(1)
        
    def end_job():
        print('Konczenie przejazdu')
        miejsca.clear()
        
        
        
        
    
    
    

print ("Aplikacja Uber ")
        
print ('''Wybeirz opcje, zalogowania
        1. Logowanie jako klient
        2. Logowanie jako kierowca''')
opcja = int(input("wybierz opcje: "))


if opcja == 1:
    print('wybrano opcje nr 1, logowanie jako klient')
    register_user()
    print('zalogowano jako: ', users)
    while True:
        print('''Prosze wybrać jedna z opcji:
              1: Wycena przejazdu
              2. Obliczanie średniego czasu przejazdu
              3. Sprawdzenie akutalnych przejazdów
              4. Rozpoczecie swoejej podrózy
              5. Historia swoich przejazdów
              6. Dodawanie swoich ulubionych adresów
              7. Udostepnienie swojej trasy kontaktowi.
              8. wylogowanie się
              9. Wylogowanie, przerwanie dzialania aplikacji''')
        
        wybor = int(input('Prosze wybrać jedna z opcji:'))
            
        if wybor == 1:
            opcje_klienta.trip_calculate()
        if wybor == 2:
            opcje_klienta.time_calculate()
        if wybor == 3:
            opcje_klienta.active_journeys()
        if wybor == 4:
            opcje_klienta.start_journey()
        if wybor == 5:
            opcje_klienta.his_trip()
        if wybor == 6:
            opcje_klienta.fav_places()
        if wybor == 7:
            opcje_klienta.share_route()
        if wybor ==8:
            opcje_klienta.logout()
        
        if wybor == 9:
            print('pomyslnie wylogowano')
            break
            

    
if opcja== 2:
    print('wybrano opcje nr 2')
    register_user()
    print('Witaj, zalogowano jako', users)
    
    
    while True:
        print('''Prosze wybrać jedna z opcji:
                1. Zacznij prace
                2. Zobacz historie przejazdow''')
        wybor1 = int(input('wybierz opcje'))
        
        
        if wybor1 == 1:
            Kierowca.start_job()
        if wybor1 == 2:
            opcje_klienta.active_journeys()
        if wybor == 3:
            Kierowca.end_job()
        if wybor == 4:
            opcje_klienta.logout()


