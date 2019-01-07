Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #309p
>>> text = '역시 파이선은 최고예요'
>>> type(text)
<class 'str'>
>>> id(text)
42638304
>>> text2 = '역시 파이선은 최고예요'
>>> type(text2)
<class 'str'>
>>> id(text2)
43087840
>>> 
>>> #310p
>>> text.__class__
<class 'str'>
>>> text.replace('파이선', 'Python')
'역시 Python은 최고예요'
>>> 
>>> #311p
>>> class BookReader:
	name = str()
	def read_book():
		print(name + ' is reading Book!!')

		
>>> 
>>> #312p
>>> reader = BookReader()
>>> type(reader)
<class '__main__.BookReader'>
>>> reader.name = 'Chris'
>>> reader.read_book()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    reader.read_book()
TypeError: read_book() takes 0 positional arguments but 1 was given
>>> 
>>> #313p
>>> class BookReader:
	name = str()
	def read_book(self):
		print(self.name + ' is reading Book!!')

		
>>> 
>>> reader = BookReader()
>>> reader.name = 'Chris'
>>> reader.read_book()
Chris is reading Book!!
>>> 
>>> #314p
>>> class BookReader:
	def __init__(self, name):
		self.name = name
	def read_book(self):
		print(self.name + ' is reading Book!!')

		
>>> 
>>> #315p
>>> reader = BookReader()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    reader = BookReader()
TypeError: __init__() missing 1 required positional argument: 'name'
>>> 
>>> BookReader('Chris')
<__main__.BookReader object at 0x0291CC50>
>>> reader.read_book()
Chris is reading Book!!
>>> 
>>> #316p
>>> class BookReader:
	country = 'South Korea'
	def __init__(self, name):
		self.name = name
	def read_book(self):
		print(self.name + ' is reading Book!!')

		
>>> 
>>> reader1 = BookReader('Chris')
>>> reader2 = BookReader('Anna')
>>> reader1.country
'South Korea'
>>> reader2.country
'South Korea'
>>> reader1.read_book()
Chris is reading Book!!
>>> reader2.read_book()
Anna is reading Book!!
>>> 
>>> #317p
>>> class Dog:
	tricks = list()
	def __init__(self, name):
		self.name = name
	def add_trick(self, trick):
		self.tricks.append(trick)

		
>>> fido = Dog('Fido')
>>> buddy = Dog('Buddy')
>>> fido.add_trick('roll over')
>>> buddy.add_trick('play dead')
>>> fido.tricks
['roll over', 'play dead']
>>> 
>>> #318p
>>> class Dog:
	def __init__(self, name):
		self.name = name
		self.tricks = list()
	def add_trick(self, trick):
		self.tricks.append(trick)

		
>>> fido = Dog('Fido')
>>> buddy = Dog('Buddy')
>>> fido.add_trick('roll over')
>>> buddy.add_trick('play dead')
>>> fido.tricks
['roll over']
>>> buddy.tricks
['play dead']
>>> 
>>> #319p
>>> random.randint(1, 10)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    random.randint(1, 10)
NameError: name 'random' is not defined
>>> 
>>> #320p
>>> import random
>>> random.randint(1,10)
8
>>> random.randint(1,10)
3
>>> random.randint(1,10)
9
>>> 
