a=0
b=1
n=int(input('몇 번째까지?:'))

for x in range(0, n):
    print(str(b)+'개','*'*b)
    c=b
    b=a+b
    a=c