# coding: utf-8

# In[1]:

#Создайте класс, осуществляющий подсчет и изменение числа книг. Названия книг, их количество считываются одной строкой вида 'Boogeyman 66 Battleground 50', число книг - произвольное.
#В классе должен быть реализован конструктор, деструктор, методы просмотра числа, взятия и возвращения книг.
#Реализовать вывод начальных значений, взятие по 1 книге, возвращение по 1 книге с выводом текущего числа после вызова каждого из методов, меняющих значение книг.
#Типичный ответ одной строкой: 'Boogeyman 66 65 66 Battleground 50 49 50'.

class Books(object):
    def __init__(self):
        self.books = {}
 
    def __del__(self):
        self.books = {}
 
    def display_book(self, book):
        self.book = book
        return self.book
 
    def take_book(self, book):
        self.book -= 1
        return self.book
        
    def put_book(self, book):
        self.book += 1
        return self.book
 
 
a = Books()
 
new_list = list(input().split())
 
for i in new_list:
    if i.isalpha():
        print(i, end=" ")
    else:
        print(a.display_book(int(i)), end=' ')
        print(a.take_book(int(i)),end=' ')
        print(a.put_book(int(i)), end=' ')


#In[2]:

#Считать одной строкой произвольное количество пар элементов "Название книги Число экземпляров", второй строкой название алгоритма хеширования md5
#Aibolit 66 Barmaley 67
#md5
#Создать 2 класса:
#1-й преобразует строку вида 'Aibolit 66 Babmaley 67', где название книги уникально, в словарь.
#2-й осуществляет хеширования названия книги алгоритмом md5.
#Вывести отдельными операторами вывода:
# - элементы словаря, отсортированные по возрастанию ключа, например:
#Aibolit 66
#Barmaley 67
# - результаты хеширования в виде пар названия алгоритма и результатов хеширования ключей, отсортированных по возрастанию, представленных в шестнадцатеричном виде, сведенных в одну строку через пробел вида
#md5 c47.... md5 5d....' (без пробелов в начале и конце строки).

import hashlib
 
# in_el = input()
# md5 = input()

class Dict(object):
 
    def __init__(self, in_el=input()):
        self.name = []
        self.count = []
        for el in in_el.split():
            if el.isdigit():
                self.count.append(int(el))
            else:
                self.name.append(el)
        self.my_dict = dict(zip(self.name, self.count))
 
    def __del__(self):
        pass
 
    def res(self):
        return self.my_dict
 
    def prin(self):
        for k in sorted(self.my_dict.keys()):
            print(k, self.my_dict[k])
 
 
class Md5(Dict):
 
    def __init__(self, md5=input()):
        self.md5 = md5
        self.d = Dict()
        self.hash_list = []
        for k in self.d.res().keys():
            self.hash_list.append(hashlib.md5(k.encode()))
 
    def __del__(self):
        pass
 
    def prin(self):
        ha_li = [el.hexdigest() for el in self.hash_list]
        # for v in sorted(self.hash_list, key=lambda x: x.digest_size):
        #     print(self.md5, v.hexdigest(), end=" ")
 
        for v in sorted(ha_li):
            print(self.md5, v, end=" ")
 
 
d = Dict()
m = Md5()
d.prin()
m.prin()


