# 11장 심화 프로젝트, 2018/05/29, 신혜민(B889041) #

def check_pwd(num):
    if num =='1234':
        return True
    else:
        return False

a = True
while a:
    x=input('비밀 번호를 입력해 주세요 : ')
    if check_pwd(x):
        a = False
    else:
        print('비밀번호가 틀렸습니다. 다시 시도합니다')
print('정확한 비밀번호 입니다!!')
