Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #158p
>>> cards = [3, 1, 5, 2]
>>> cards
[3, 1, 5, 2]
>>> type(cards)
<class 'list'>
>>> 
>>> #159p
>>> cards[0]
3
>>> cards[3]
2
>>> 
>>> cards[-1]
2
>>> 
>>> #160p
>>> len(cards)
4
>>> 
>>> cards[4]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    cards[4]
IndexError: list index out of range
>>> 
