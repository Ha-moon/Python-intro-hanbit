text = input('문자열을 입력하세요 : ')       # 문자열 입력

origin = text.replace(' ', '')                     # 문자열 공백 제거
reverse = str()                                       # 역순 문자열 변수 생성

index = len(origin) - 1                            # 마지막 색인 추출

while index >= 0:                                    # 색인이 0이 될 때까지 반복
    
    reverse += origin[index]                    # 역순으로 문자 적재
    
    index -= 1                                           # 색인 감소

if origin == reverse:                                 # 두 변수 값이 같으면 회문

    print('입력하신 문장은 회문이 맞습니다.')

else:                                                       # 같지 않으면 회문이 아님

    print('입력하신 문장은 회문이 아닙니다.')
