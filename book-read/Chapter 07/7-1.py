text = input('영어 대소문자로 이루어진 문장을 입력하세요.\n')  # 문자열 입력

print('\n모두 대문자로 변경\n' + text.upper())   # 대문자로 모두 변환

print('\n모두 소문자로 변경\n' + text.lower())   # 소문자로 모두 변환

new_text = str()                                    # 신규 문자열 형 변수 선언

for c in text:                                          # 입력 받은 문자 순회

    if c.islower():                                    # 해당 문자가 소문자이면
        new_text += c.upper()                   # 대문자로 변경하여 신규 문자열에 붙이기
    else:                                                 # 해당 문자가 대문자이면
        new_text += c.lower()                   # 소문자로 변경하여 신규 문자열에 붙이기

print('\nfor문과 if문 사용하여 대소문자 변경\n' + new_text)             # 최종 변환 결과 출력

print('\n소스 코드 한 줄로 대소문자 변경\n' + text.swapcase())      # 대소문자 모두 변환
