# coding: utf-8

# In[1]:

#Создайте класс, осуществляющий подсчет и изменение числа книг. Названия книг, их количество считываются одной строкой вида 'Boogeyman 66 Battleground 50', число книг - произвольное.
#В классе должен быть реализован конструктор, деструктор, методы просмотра числа, взятия и возвращения книг.
#Реализовать вывод начальных значений, взятие по 1 книге, возвращение по 1 книге с выводом текущего числа после вызова каждого из методов, меняющих значение книг.
#Типичный ответ одной строкой: 'Boogeyman 66 65 66 Battleground 50 49 50'.

class Library(object):
    def __init__(self):
        self.books = {}
 
    def __del__(self):
        self.books = {}
 
    def get_quantity(self, book):
        print(self.books[book], end=' ')
 
    def get_book(self, book):
        self.books[book] -= 1
        print(self.books[book], end=' ')
 
    def return_book(self, book):
        self.books[book] += 1
        print(self.books[book], end=' ')
 
 
a = Library()
books_init = input().split()
 
for i in range(0, len(books_init), 2):
    a.books[books_init[i]] = int(books_init[i + 1])
 
for book in a.books:
    print(book, end=' ')
    a.get_quantity(book)
    a.get_book(book)
    a.return_book(book)
