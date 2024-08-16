# coding: utf-8

# In[1]:

#Считать с клавиатуры полный адрес англоязычной html страницы.
#С использованием urlparse получить из адреса кортеж значений.
#Вывести текст всех заголовков уровня h1 одной строкой через пробел без дополнительных символов вначале и конце строки.
#Примечание. Если внутри тегов h1 содержатся ссылки, то нужно выводить вместе со ссылками.

#Пример входных данных:
#http://en.ifmo.ru/en/contacts/Contacts.htm

#Пример выходных данных:
#('http', 'en.ifmo.ru', '/en/contacts/Contacts.htm', '', '', '')
#Contacts

from urllib.parse import urlparse
import urllib.request as r

print('адрес html страницы:')
url = input()
url_res=urlparse(url)
print(tuple(url_res))
 
page = r.urlopen(url)
 
pr=page.read().decode('utf-8')
list_h1 = []
if '<h1>' in pr:
    h1=pr.split('<h1>')
 
    for h in h1:
        if '</h1>' in h:
            list_h1.append(h.split('</h1>')[0])
    print(' '.join(list_h1))




