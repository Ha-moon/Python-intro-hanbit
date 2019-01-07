Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #269p
>>> def hello():
	name = input('이름을 입력하세요! ')
	print('안녕!', name)

	
>>> hello()
이름을 입력하세요! 신후
안녕! 신후
>>> 
>>> #271p
>>> def hello(name):
	print('안녕!', name)

	
>>> my_name = input('이름을 입력하세요! ')
이름을 입력하세요! 안나
>>> hello(my_name)
안녕! 안나
>>> 
>>> #272p
>>> def sum(a, b):
	print(a+b)

	
>>> sum(1, 4)
5
>>> sum(7, 3)
10
>>> 
>>> #273p
>>> def change_name(name):
	return name + '님'

>>> change_name('지희')
'지희님'
>>> 
>>> #274p
>>> def my_func(param):
	param = '함수 안에서 생성'
	print(param)

	
>>> param = '함수 밖에서 생성'
>>> my_func(param)
함수 안에서 생성
>>> print(param)
함수 밖에서 생성
>>> 
>>> #276p
>>> del param
>>> def my_func():
	global param
	param = '함수 안에서 변경'
	print(param)

	
>>> param = '함수 밖에서 생성'
>>> my_func()
함수 안에서 변경
>>> print(param)
함수 안에서 변경
>>> 
>>> 
