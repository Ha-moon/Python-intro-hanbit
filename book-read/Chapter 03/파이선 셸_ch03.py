Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #75p
>>> hello = '안녕, 파이선!'
>>> print(hello)
안녕, 파이선!
>>> 
>>> type(hello)
<class 'str'>
>>> 
>>> #76p
>>> hello1 = '안녕, 파이선!'
>>> print(hello1)
안녕, 파이선!
>>> hello2 = "안녕, 파이선!"
>>> print(hello2)
안녕, 파이선!
>>> 
>>> #77p
>>> hello = '안녕
SyntaxError: EOL while scanning string literal
>>> hello = 안녕'
SyntaxError: EOL while scanning string literal
>>> hello = "안녕
SyntaxError: EOL while scanning string literal
>>> hello = 안녕"
SyntaxError: EOL while scanning string literal
>>> 
>>> #78p
>>> hello = 안녕
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    hello = 안녕
NameError: name '안녕' is not defined
>>> 
>>> #79p
>>> guide = '작은따옴표(')를 문자열 시작과 끝에 붙인다.'
SyntaxError: invalid syntax
>>> 
>>> #81p
>>> text = '''실패하는 것보다
도전하지 않는 것을
두려워하라.'''
>>> print(text)
실패하는 것보다
도전하지 않는 것을
두려워하라.
>>> 
>>> #83p
>>> name = input('이름을 입력하세요: ')
이름을 입력하세요: 조인석
>>> welcome = name + '님, 반갑습니다'
>>> print(welcome)
조인석님, 반갑습니다
>>> 
>>> #84p
>>> cheer = '파이팅! ' * 3
>>> print(cheer)
파이팅! 파이팅! 파이팅! 
>>> 
>>> #86p
>>> len('파이선 프로그래밍은 즐겁다.')
15
>>> text = '쉽고 재미있는 파이선 프로그래밍'
>>> len(text)
17
>>> 
>>> #88p
>>> word = 'Python'
>>> word.upper();
'PYTHON'
>>> word.lower();
'python'
>>> '-'.join(word)
'P-y-t-h-o-n'
>>> print(word)
Python
>>> 
