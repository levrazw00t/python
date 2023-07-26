# coding: utf-8

# In[1]:

h=input()

import hashlib

h2={'md5':(hashlib.md5(h.encode())).hexdigest(),
    'sha1':(hashlib.sha1(h.encode())).hexdigest(),
    'sha224':(hashlib.sha224(h.encode())).hexdigest(),
    'sha224':(hashlib.sha224(h.encode())).hexdigest(),
    'sha256':(hashlib.sha256(h.encode())).hexdigest(),
    'sha384':(hashlib.sha384(h.encode())).hexdigest(),
    'sha512':(hashlib.sha224(h.encode())).hexdigest()}

for key, value in sorted(h2.items()):
    print(key, value)
