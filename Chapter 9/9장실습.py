# 9장 실습 프로젝트, 2018/05/08, 신혜민(B889041)

count = int(input('입력하는 학생수가 총 몇명인가요? : '))

print('학생의 이름과 시험 점수를 차례대로 입력하세요!')

num=1
program_list=[]

while num<= count:
    print(num,'번째 학생=====')
    name=input('*이름: ')
    score=int(input('*점수: '))
    program_list=program_list+[(name,score)]
    num=num+1

scores_dict=dict(program_list)

flag=True
while flag:
    wanted=input('어떤 학생의 점수가 궁금하신가요? 이름을 입력하세요. :')

    if wanted in scores_dict:
        print(wanted,'학생의 점수 :',scores_dict[wanted])
        print('프로그램을 종료합니다.')
        flag=False
    else:
        print('찾는 학생(',wanted,')의 점수가 존재하지 않습니다.')
