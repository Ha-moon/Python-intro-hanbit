print('##')
a=float(input('X축'))
b=float(input('Y축'))
if a>0 and b>0:
    print('1사분면')
elif a>0 and b<0:
    print('4사분면')
elif a<0 and b>0:
    print('2사분면')
elif a<0 and b<0:
    print('3사분면')
elif a==0 and b==0:
    print('원점이다.')
else:
    print('정수를 입력하세요')