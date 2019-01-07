Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #289p
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(1, 6))
[1, 2, 3, 4, 5]
>>> list(range(1, 11, 2))
[1, 3, 5, 7, 9]
>>> 
>>> def weekly_working_hours(hours):
	return hours

>>> weekly_working_hours(40)
40
>>> weekly_working_hours(50)
50
>>> weekly_working_hours()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    weekly_working_hours()
TypeError: weekly_working_hours() missing 1 required positional argument: 'hours'
>>> 
>>> #290p
>>> def weekly_working_hours(hours=40):
	return hours

>>> weekly_working_hours()
40
>>> 
>>> #291p
>>> def print_student_info(name, birth, major='CS', country='KOR'):
	print('이름 :', name,', 생년월일 :', birth,', 전공 :', major, ', 국적 :', country)

	
>>> 
>>> #292p
>>> print_student_info('조안나', '19981215')
이름 : 조안나 , 생년월일 : 19981215 , 전공 : CS , 국적 : KOR
>>> print_student_info('조안나', '19981215', 'ME')
이름 : 조안나 , 생년월일 : 19981215 , 전공 : ME , 국적 : KOR
>>> print_student_info('조안나', '19981215', 'EE', 'USA')
이름 : 조안나 , 생년월일 : 19981215 , 전공 : EE , 국적 : USA
>>> 
>>> print_student_info('조안나', '19981215', country='AUS')
이름 : 조안나 , 생년월일 : 19981215 , 전공 : CS , 국적 : AUS
>>> 
>>> print_student_info(country='UK', birth='19950820', name='Andy Shanks', major='EE')
이름 : Andy Shanks , 생년월일 : 19950820 , 전공 : EE , 국적 : UK
>>> 
>>> print_student_info()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print_student_info()
TypeError: print_student_info() missing 2 required positional arguments: 'name' and 'birth'
>>> 
>>> #293p
>>> print_student_info('김건아')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print_student_info('김건아')
TypeError: print_student_info() missing 1 required positional argument: 'birth'
>>> 
>>> print_student_info('김건아', '19980312', name='김건아')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print_student_info('김건아', '19980312', name='김건아')
TypeError: print_student_info() got multiple values for argument 'name'
>>> 
>>> print_student_info('김건아', '19980312', language='English')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print_student_info('김건아', '19980312', language='English')
TypeError: print_student_info() got an unexpected keyword argument 'language'
>>> 
>>> #294p
>>> def print_language(*languages):
	for lang in languages:
		print(lang)

		
>>> print_language('Python', 'Java', 'Ruby')
Python
Java
Ruby
>>> 
>>> def print_language_tuple(languages_tuple):
	for lang in languages_tuple:
		print(lang)

		
>>> print_language_tuple(('Python', 'Java', 'Ruby'))
Python
Java
Ruby
>>> 
>>> #295p
>>> def map_student_language(**student_language):
	for name in student_language.keys():
		print(name, student_language[name])

		
>>> map_student_language(인석='Python', 치훈='Java', 수빈='JavaScript')
인석 Python
치훈 Java
수빈 JavaScript
>>> 
>>> #296p
>>> def concat(*args, sep='/'):
	return sep.join(args)

>>> concat('a', 'b', 'c')
'a/b/c'
>>> concat('a', 'b', 'c', sep='.')
'a.b.c'
>>> concat( sep='-', 'a', 'b', 'c',)
SyntaxError: positional argument follows keyword argument
>>> 
>>> #298p
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> args = 5, 10
>>> list(range(*args))
[5, 6, 7, 8, 9]
>>> 
>>> def print_student_info(name, birth, major='CS', country='KOR'):
	print('이름 :', name, ', 생년월일 :', birth, ', 전공 :', major, ', 국적 :', country)

	
>>> info = {'name': '김강우', 'birth': '19990802'}
>>> print_student_info(**info)
이름 : 김강우 , 생년월일 : 19990802 , 전공 : CS , 국적 : KOR
>>> 
