Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #217p
>>> text = '파이선 문자열'
>>> text[0]
'파'
>>> text[-1]
'열'
>>> 
>>> #218p
>>> text[-1] = '다'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    text[-1] = '다'
TypeError: 'str' object does not support item assignment
>>> 
>>> #219p
>>> card = 'red', 4, '다이아몬드', True
>>> card
('red', 4, '다이아몬드', True)
>>> card[-1] = False
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    card[-1] = False
TypeError: 'tuple' object does not support item assignment
>>> 
>>> #220p
>>> card[2]
'다이아몬드'
>>> card[:2]
('red', 4)
>>> card[2:]
('다이아몬드', True)
>>> card[:]
('red', 4, '다이아몬드', True)
>>> 
>>> #222p
>>> a, b, c, d = card
>>> a
'red'
>>> b
4
>>> c
'다이아몬드'
>>> d
True
>>> 
>>> #225p
>>> languages = {'C++', 'Python', 'C', 'C', 'C++', 'Python'}
>>> languages
{'Python', 'C', 'C++'}
>>> 'Python' in languages
True
>>> 'R' in languages
False
>>> 
>>> #226p
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a
{'c', 'd', 'b', 'a', 'r'}
>>> a - b
{'d', 'r', 'b'}
>>> a | b
{'c', 'd', 'b', 'l', 'a', 'z', 'm', 'r'}
>>> a & b
{'c', 'a'}
>>> a ^ b
{'b', 'd', 'z', 'm', 'r', 'l'}
>>> 
>>> #228p
>>> programmer_dict= {'Python':5, 'C':2, 'C++':3, 'Java':4}
>>> programmer_dict
{'Python': 5, 'C': 2, 'C++': 3, 'Java': 4}
>>> type(programmer_dict)
<class 'dict'>
>>> programmer_dict['Python']
5
>>> 
>>> programmer_dict['Python'] = 7
>>> programmer_dict
{'Python': 7, 'C': 2, 'C++': 3, 'Java': 4}
>>> 
>>> #229p
>>> programmer_dict['Ruby'] = 1
>>> programmer_dict
{'Python': 7, 'C': 2, 'C++': 3, 'Java': 4, 'Ruby': 1}
>>> 
>>> len(programmer_dict)
5
>>> 
>>> programmer_dict.keys()
dict_keys(['Python', 'C', 'C++', 'Java', 'Ruby'])
>>> list(programmer_dict.keys())
['Python', 'C', 'C++', 'Java', 'Ruby']
>>> 
>>> #230p
>>> list(programmer_dict.values())
[7, 2, 3, 4, 1]
>>> 
>>> 'Python' in programmer_dict
True
>>> 'Swift' in programmer_dict
False
>>> 'R' not in programmer_dict
True
>>> 
>>> programmer_dict
{'Python': 7, 'C': 2, 'C++': 3, 'Java': 4, 'Ruby': 1}
>>> del programmer_dict['Ruby']
>>> programmer_dict
{'Python': 7, 'C': 2, 'C++': 3, 'Java': 4}
>>> 
>>> programmer_dict.clear()
>>> programmer_dict
{}
>>> 
>>> #231p
>>> programmer_list = [('Python', 7), ('Java', 2)]
>>> programmer_list
[('Python', 7), ('Java', 2)]
>>> 
>>> programmer_dict = dict(programmer_list)
>>> type(programmer_dict)
<class 'dict'>
>>> programmer_dict
{'Python': 7, 'Java': 2}
>>> 
>>> #232p
>>> programmer_dict['Python']
7
>>> programmer_dict['Java']
2
>>> 
