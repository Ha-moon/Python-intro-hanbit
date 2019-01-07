win_a=0
win_b=0
while win_a<3 and win_b<3:
    user_a=input('안나를 위한:')
    user_b = input('신후를 위한:')

    if user_a == '가위':
        if user_b == '바위':
            print('신후승리')
            win_b = win_b + 1
        elif user_b == '보':
            print('안나승리')
            win_a = win_a + 1
    print('안나', win_a,':', '신후',win_b)
if win_a > win_b :
    print('###안나 3선승!')
elif win_a < win_b :
    print('###신후 3선승!')