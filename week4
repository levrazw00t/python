# coding: utf-8

# In[1]:

#Создайте класс, осуществляющий подсчет и изменение числа книг. Названия книг, их количество считываются одной строкой вида 'Boogeyman 66 Battleground 50', число книг - произвольное.
#В классе должен быть реализован конструктор, деструктор, методы просмотра числа, взятия и возвращения книг.
#Реализовать вывод начальных значений, взятие по 1 книге, возвращение по 1 книге с выводом текущего числа после вызова каждого из методов, меняющих значение книг.
#Типичный ответ одной строкой: 'Boogeyman 66 65 66 Battleground 50 49 50'.

class Books(object):
 
    def __init__(self):
        pass
 
    def __del__(self):
        pass
 
    def display_book(self, book):
        self.book = book
        return self.book
 
    def take_one_book(self, book):
        self.book = book - 1
        return self.book
    def put_one_book(self, book):
        self.book = book + 1
        return self.book
 
 
a = Books()
 
new_list = list(input().split())
 
for i in new_list:
    if i.isalpha():
        print(i, end=" ")
    if i.isdigit():
        print(a.display_book(int(i)), end=" ")
        print(a.take_one_book(a.display_book(int(i))), end=" ")
        print(a.put_one_book(a.take_one_book(a.display_book(int(i)))), end=" ")
