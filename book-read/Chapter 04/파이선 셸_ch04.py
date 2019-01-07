Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #101p
>>> type(100)
<class 'int'>
>>> type(100.0)
<class 'float'>
>>> 
>>> #102p
>>> 243 + 792
1035
>>> 
>>> #103p
>>> 10000 - 1035
8965
>>> 
>>> 500 * 243
121500
>>> 100 * 792
79200
>>> 500 * 243 + 100 * 792
200700
>>> 
>>> #105p
>>> 121500 / 200700
0.6053811659192825
>>> 
>>> #106p
>>> 200700 // 500
401
>>> 200700 % 500
200
>>> 
>>> #107p
>>> total_count = 243 + 792
>>> total_price = (500 * 243) + (100 * 792)
>>> 
>>> print(total_count)
1035
>>> print(total_price)
200700
>>> 
>>> #108p
>>> total_count = 243 + 792
>>> init_count = final_count = total_count
>>> print(total_count)
1035
>>> print(init_count)
1035
>>> print(final_count)
1035
>>> 
>>> #109p
>>> print("초기 개수: ", final_count)
초기 개수:  1035
>>> final_count = final_count + 1
>>> print("증가 후 개수: ", final_count)
증가 후 개수:  1036
>>> 
>>> final_count += 1
>>> print("증가 후 개수: ", final_count)
증가 후 개수:  1037
>>> 
>>> #113p
>>> 100 + int('100')
200
>>> 
>>> str(100) + '100'
'100100'
>>> 
