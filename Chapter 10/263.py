# 10장 심화 프로젝트I, 2018/05/15, 신혜민(B889041) #

print('지금부터 달리기 시합을 시작하겠습니다.\n')
count = int(input('달리기 선수가 몇명인가요? : '))

num=1
program_list=[]

while num<= count:
    name=input('\n지금 들어온 선수 이름을 입력하세요 : ')
    program_list=program_list+[(name)]
    num=num+1

print('\n달리기 시합 결과!!\n')

program_list_enum=enumerate(program_list)
for index, name in program_list_enum:
    print(index+1,'등', name)

print('\n수고 많았습니다, 여러분!!')

