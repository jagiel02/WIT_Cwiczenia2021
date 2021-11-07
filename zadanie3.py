#1
def convert_string_to_number():
    x = input('wprowadz stringa')
    print(int(x))


convert_string_to_number()

#2
def find_min():

    lista = [34, 21, 90, 14]

    for i in lista:
        if i < int(lista[1]):
            print(i)

find_min()

#3

list2 = [1,2,3,4,5]
def print_list():
    for i in list2:
        print(i)

print_list()


#4

def print_dict():
    slownik= {
        "a" : 1,
        "b" : 2,
        "c" : 3
    }

    print(slownik)

print_dict()


#5

def get_lenght():
    x = input('wprowadz slowo')
    return print (len(x))

get_lenght()




#6
def odwrot():
  s = input('wprowadz stringa: ')
  z = ""
  for i in s:
    z = s[1:]
  return z

print (odwrot())



#7

def count_chars():
    q = {}
    slowo = 'przyklad'

    for tekst in slowo:
        q.update({tekst: 1})
    return q

print(count_chars())
