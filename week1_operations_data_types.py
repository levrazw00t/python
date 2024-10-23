# coding: utf-8

# In[1]:

# Считать отдельными операторами два целых числа, получить: сумму, разность, результат целочисленного деления, 
# частное, остаток от деления, третью степень первого числа и вторую степень второго числа и вывести их отдельными операторами вывода.

a = int(input())
b = int(input())

print(a + b)     
print(a - b)     
print(a // b)    
print(a / b)
print(a % b)   
print(a ** 3)    
print(b ** 2)    

# In[2]:

# Считать несколько имен людей одной строкой, записанных латиницей, через пробел, например: «Anna Maria Peter» 
# Вывести их одной строкой в порядке возрастания «Anna Maria Peter».
# Вывести их одной строкой в порядке убывания «Peter Maria Anna».

a = str(input())

list1 = sorted(a.split())
print(' '.join(list1))

list2 = list1[::-1]
print(' '.join(list2))


# In[3]:

# Считать единой строкой без пробелов набор целых чисел (28745623873465386), 
# удалить все дубликаты, вывести отдельными операторами вывода в порядке возрастания 
# и в порядке убывания в виде кортежей целых чисел (2, 3, 4, 5, 6, 7, 8) и (8, 7, 6, 5, 4, 3, 2)

a = input()

# set может содержать только уникальные значения. приводим множество к списку и сортируем его в порядке возрастания
list1 = sorted(list(set(a)))       

# преобразуем список в кортеж целых чисел и выводим результат
print(tuple(map(int, list1)))

# меняем порядок элементов списка на противоположный
list2 = list1[::-1]

# преобразуем перевернутый список в кортеж целых чисел и выводим результат
print(tuple(map(int, list2)))

