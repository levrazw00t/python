# coding: utf-8

# In[1]:

#Ввести с клавиатуры строку латиницей (1-3 слова). Зашифровать ее с использованием гарантированных алгоритмов шифрования. 
#Сформировать словарь, где в качестве ключа используется название гарантированного алгоритма шифрования, 
#а в качестве значения - результат шифрования в шестнадцатеричном представлении { 'sha1': 'd0b…', 'md5', '1f3…',…}.
#Итог вывести отдельными операторами вывода в виде пар ключа и значения, отсортированных по возрастанию ключа:
#md5 1f3…
#sha1 d0b…

h=input()

import hashlib

h2={'md5':(hashlib.md5(h.encode())).hexdigest(),
    'sha1':(hashlib.sha1(h.encode())).hexdigest(),
    'sha224':(hashlib.sha224(h.encode())).hexdigest(),
    'sha256':(hashlib.sha256(h.encode())).hexdigest(),
    'sha384':(hashlib.sha384(h.encode())).hexdigest(),
    'sha512':(hashlib.sha512(h.encode())).hexdigest()}

for key, value in sorted(h2.items()):
    print(key, value)
