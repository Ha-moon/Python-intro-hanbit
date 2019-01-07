Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #245p
>>> nums = 4, 2, 5, 7, 1, 3
>>> sorted(nums)
[1, 2, 3, 4, 5, 7]
>>> sorted(nums, reverse = True)
[7, 5, 4, 3, 2, 1]
>>> nums
(4, 2, 5, 7, 1, 3)
>>> 
>>> #246p
>>> programmer_dict= {'Python':5, 'C':2, 'C++':3, 'Java':4, 'Ruby':1}
>>> sorted(programmer_dict.keys())
['C', 'C++', 'Java', 'Python', 'Ruby']
>>> sorted(programmer_dict.keys(), reverse = True)
['Ruby', 'Python', 'Java', 'C++', 'C']
>>> 
>>> #247p
>>> nums = 0, 1, 2, 3, 4
>>> for num in nums:
	print(num)

	
0
1
2
3
4
>>> 
>>> #248p
>>> for num in range(5):
	print(num)

	
0
1
2
3
4
>>> 
>>> for num in range(1, 6):
	print(num)

	
1
2
3
4
5
>>> 
>>> #249p
>>> for num in range(1, 11, 2):
	print(num)

	
1
3
5
7
9
>>> 
>>> for num in range(2, 11, 2):
	print(num)

	
2
4
6
8
10
>>> langs = 'python', 'java', 'C++'
>>> for index in range(len(langs)):
	print(index, langs[index])

	
0 python
1 java
2 C++
>>> 
>>> #250p
>>> squares = []
>>> for x in range(10):
	squares.append(x**2)

	
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> new_squares = [x**2 for x in range(10)]
>>> new_squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> #251p
>>> A = ['blue', 'yellow', 'red']
>>> B = ['red', 'green', 'blue']
>>> pairs = []
>>> for a in A:
	for b in B:
		if a != b:
			pairs.append((a, b))

			
>>> pairs
[('blue', 'red'), ('blue', 'green'), ('yellow', 'red'), ('yellow', 'green'), ('yellow', 'blue'), ('red', 'green'), ('red', 'blue')]
>>> 
>>> #252p
>>> new_pairs = [(a, b) for a in A for b in B if a!= b]
>>> new_pairs
[('blue', 'red'), ('blue', 'green'), ('yellow', 'red'), ('yellow', 'green'), ('yellow', 'blue'), ('red', 'green'), ('red', 'blue')]
>>> 
>>> #253p
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'d', 'r'}
>>> 
>>> #254p
>>> square_dic = {x: x**2 for x in (2, 4, 6)}
>>> square_dic
{2: 4, 4: 16, 6: 36}
>>> 
>>> #255p
>>> korean_foods = ['kimchi', 'bibimbab', 'tteok-bokki']
>>> 
>>> korean_foods[0]
'kimchi'
>>> 
>>> index = 0
>>> for food in korean_foods:
	print(index, food)
	index += 1

	
0 kimchi
1 bibimbab
2 tteok-bokki
>>> 
>>> #256p
>>> korean_foods_enum = enumerate(korean_foods)
>>> type(korean_foods_enum)
<class 'enumerate'>
>>> 
>>> for index, food in korean_foods_enum:
	print(index, food)

	
0 kimchi
1 bibimbab
2 tteok-bokki
>>> 
>>> 
