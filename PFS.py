Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a,b,c=10,20,30
>>> print(a)
10
>>> print(b)
20
>>> print
<built-in function print>
>>> print(c)
30
>>> a=b=c=10
>>> print(a)
10
>>> print(b)
10
>>> print(c)
10
>>> print(id(a))        #address
140719679464520
>>> print(id(b))
140719679464520
>>> a,b=257,257
>>> print(id(a), id(b))
1366003121552 1366003121552
>>> a,b=10,20
>>> a,b=b,a
>>> print(id(a), id(b))
140719679464840 140719679464520
>>> print(a,b)
20 10
>>> a,b=10,20
>>> print(id(a), id(b))
140719679464520 140719679464840
