# 가위-바위-보 리스트 선언
all = ['가위', '바위', '보']

# 바깥쪽 for 문
for user_a in all:

    # 안쪽 for 문
    for user_b in all:

        # 결과 출력
        print(user_a, 'vs', user_b)
