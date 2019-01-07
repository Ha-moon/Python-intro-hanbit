# 11장 실습 프로젝트, 2018/05/29, 신혜민(B889041) #

def multiple(num):
    for x in range(1, 10):
        print(num,'X',x,'=',num*x)
        
for n in range(1, 10):
    print('\n-',n,'단---')
    multiple(n)
