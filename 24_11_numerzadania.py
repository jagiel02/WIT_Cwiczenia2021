
def calc_circle_area(n):
    print(3.14 * (int(n)*int(n)))


calc_circle_area(3)



def check_parity():
    number = int(input('wprowadz liczbe'))

    if number % 2 == 0:
        print('Parzysta')
    else:
        print('nieparzysta')


check_parity()


def listy(x, z):
    for i in z:
        if x == i:
            return print(True)
    return print(False)


print(listy(2, [1, 2, 3, 4]))




def check_str_len():
    string = (input('wprowadz slowo'))

    if len(string) >= 8:
        print('true')
    else:
        raise ValueError('za krotkie slowo')


check_str_len()

slownik = {}
def print_menu():
    print('1. Dodaj wpis')
    print('2. Odzyskaj wpis')
    print('3. Zmodyfikuj wpis')
    print('4. Usu? wpis')
    print('0. Wyjd?')

def create_item():
    a = input('dodaj wpis: ')
    slownik[''] = a
    pass

def read_item():
    print(slownik)
    pass


def update_item():
    b = input('zaktualizuj wpis')
    slownik[''] = b
    pass


def delete_item():
    slownik.clear()
    pass

while True:
    print_menu()
    option = input("Podaj opcj?: ")
    if option == '1':
        create_item()
        pass
    elif option == '2':
        read_item()
        pass
    elif option == '3':
        update_item()
        pass
    elif option == '4':
        delete_item()
        pass
    elif option == '0':
        break


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        pass
    def set_name(self):
        pass

animal1 = Animal("a")
animal1.get_name()
animal1.set_name()


class Mammal(Animal):
    def __init__(self, name, no_legs, has_fur):
        super().__init__(name)
        self.no_legs = no_legs
        self.has_fur = has_fur


    def get_no_legs(self):
        pass

    def set_no_legs(self):
        pass

    def get_has_fur(self):
        pass

    def set_has_fur(self):
        pass


Mammal1 = Mammal('a', 'b', 'c')
Mammal1.get_name()
Mammal1.set_no_legs()
Mammal1.get_has_fur()
Mammal1.set_has_fur()


class Caine(Mammal):
    def __init__(self, name, no_legs, has_fur, howl, bark):
        super().__init__(name, no_legs, has_fur)
        self.howl = howl
        self.bark = bark



class Dog(Caine):
    def __init__(self, name, no_legs, has_fur, howl, bark, kind, owner):
        super().__init__(name, no_legs, has_fur, howl, bark)
        self.kind = kind
        self.owner = owner


    def get_kind(self):
        pass
    def set_kind(self):
        pass
    def get_owner(self):
        pass
    def set_owner(self):
        pass

Dog1 = Dog('a','b','c','d', 'e', 'f', 'g')

Dog1.get_kind()
Dog1.set_kind()
Dog1.get_owner()
Dog1.set_owner()
