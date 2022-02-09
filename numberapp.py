import sqlite3
from pprint import pprint
from urllib import response
from matplotlib.pyplot import connect
from numpy import logspace, number
import requests
from datetime import datetime




connect = sqlite3.connect('numberapp.db')
cursor = connect.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (username, password, requests_count)' )

cursor.execute('CREATE TABLE IF NOT EXISTS logs (date, type_param, number_param)')
connect.close()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

                
    '''
    username: nazwa użytkownika,
    password: hasło użytkownika,
    requests_count: ilość requestów wykonanych przez użytkownika
    '''
class Log:
    def __init__(self, date, type_param, number_param):
        self.type_param = type_param
        self.number_param = number_param
        self.date = date
        
        
    def date():
        now = datetime.datetime.now()
        print(now)
        
    '''
    username: nazwa użytkownika k†óry wykonał zapytanie,
    date: data kiedy zapytanie zostało wykonane
    type_param: co użytkownik wybrał jako `type`,
    number_param: co użytkownik wybrał jako `number` 
    '''


def register():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    username = input('podaj login: ')
    password = input('wpisz haslo: ')
    response = requests.get('http://numbersapi.com/')
    status = response.status_code 
    connect = sqlite3.connect('numberapp.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (username, password, status))
    cursor.execute('INSERT INTO logs(date) VALUES(?)',[current_time])
    queryset = cursor.execute('SELECT * FROM users')
    users = queryset.fetchall()
    queryset2 = cursor.execute('SELECT date FROM logs')
    logs = queryset2.fetchall()
    print(users, logs)
    connect.commit()
    connect.close()

def login():
    username = input('podaj login: ')
    password = input('wpisz haslo: ')
    connect = sqlite3.connect('numberapp.db')
    cursor = connect.cursor()
    queryset = cursor.execute('SELECT * from users')
    users = queryset.fetchall()
    connect.close()
    users_object = []
    
    for user in users:
        users_object.append(User(user[0], user[1]))
        
    for user in users_object:
        if user.username == username and user.password == password:
            return user
    return False




def get_number():
    number = input('wprowadz swoj numer')
    type = input('wprowadz swoj type: ')
    response = requests.get(f'http://numbersapi.com/{number}/{type}/date')
    data = response.json()
    pprint(data)
    
    
    
    
    

def get_logs():
    pass

def get_users():
    pass 


user = False
while True:
    if not user:
        print('1. Zarejestruj się')
        print('2. Zaloguj się')
        print('0. Wyjdź z programu')
        option = input('Podaj opcję: ')
        if option == '1':
            register()
        elif option == '2':
            user = login()
        elif option == '0':
            break
    else:
        print('1. Wykonaj zapytanie')
        print('2. Zobacz logi')
        print('3. Zobacz uzytkowników')
        print('0. Wyjdź z programu')
        option = input('Podaj opcję: ')
        if option == '1':
            get_number()
        elif option == '2':
            get_logs()
        elif option == '3':
            get_users()
        elif option == '0':
            break


