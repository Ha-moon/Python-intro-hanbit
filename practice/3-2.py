print('구구단입니다.')
a=int(input(">>>"))
b=int(input(">>>"))
while a<1 or a>9 or b<1 or b>9 or a>b:
    print('제대로 된 값을 입력하세요.')
    a=int(input(">>>"))
    b=int(input(">>>"))
for x in range(a,b+1):
    print(str(x)+'단 입니다.')
    for y in range(1,10):
        print(x,'X',y,'=',x*y)