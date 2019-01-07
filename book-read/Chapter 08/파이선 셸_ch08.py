Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #189p
>>> cards = [3, 1, 5, 2]
>>> cards
[3, 1, 5, 2]
>>> type(cards)
<class 'list'>
>>> cards[0]
3
>>> cards[3]
2
>>> cards[-1]
2
>>> cards[4]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    cards[4]
IndexError: list index out of range
>>> 
>>> #190p
>>> cards
[3, 1, 5, 2]
>>> 
>>> cards[1] = 8
>>> cards
[3, 8, 5, 2]
>>> 
>>> #191p
>>> cards
[3, 8, 5, 2]
>>> cards.append(7)
>>> cards
[3, 8, 5, 2, 7]
>>> 
>>> cards
[3, 8, 5, 2, 7]
>>> cards.remove(5)
>>> cards
[3, 8, 2, 7]
>>> 
>>> #192p
>>> cards
[3, 8, 2, 7]
>>> cards.insert(1, 9)
>>> cards
[3, 9, 8, 2, 7]
>>> 
>>> #193p
>>> cards
[3, 9, 8, 2, 7]
>>> cards.pop(3)
2
>>> cards
[3, 9, 8, 7]
>>> 
>>> #195p
>>> cards
[3, 9, 8, 7]
>>> cards[1:3]
[9, 8]
>>> 
>>> cards[:2]
[3, 9]
>>> cards[1:]
[9, 8, 7]
>>> 
>>> #196p
>>> cards
[3, 9, 8, 7]
>>> 
>>> sub_cards = cards[1:3]
>>> sub_cards
[9, 8]
>>> 
>>> cards
[3, 9, 8, 7]
>>> new_cards = cards
>>> new_cards.append(2)
>>> new_cards
[3, 9, 8, 7, 2]
>>> 
>>> #197p
>>> cards
[3, 9, 8, 7, 2]
>>> 
>>> #198p
>>> cards
[3, 9, 8, 7, 2]
>>> new_cards = cards[:]
>>> new_cards.append(5)
>>> new_cards
[3, 9, 8, 7, 2, 5]
>>> cards
[3, 9, 8, 7, 2]
>>> 
>>> #200p
>>> a = [1, 2]
>>> b = [3, 4]
>>> c = a + b
>>> a
[1, 2]
>>> b
[3, 4]
>>> c
[1, 2, 3, 4]
>>> 
>>> a.extend(b)
>>> a
[1, 2, 3, 4]
>>> 
>>> #201p
>>> a
[1, 2, 3, 4]
>>> del a[0]
>>> a
[2, 3, 4]
>>> del a[1:3]
>>> a
[2]
>>> del a[:]
>>> a
[]
>>> 
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
>>> #203p
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> matrix[0]
[1, 2, 3]
>>> matrix[1]
[4, 5, 6]
>>> matrix[1][1]
5
>>> matrix[2][2]
9
>>> 
>>> #204p
>>> dice = [1, 2, 3, 4, 5, 6]
>>> type(dice)
<class 'list'>
>>> 
>>> empty_list = []
>>> empty_list
[]
>>> type(empty_list)
<class 'list'>
>>> 
>>> empty_list_2 = list()
>>> empty_list_2
[]
>>> type(empty_list_2)
<class 'list'>
>>> 
