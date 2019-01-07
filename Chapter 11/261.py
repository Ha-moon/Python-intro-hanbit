# 10장 실습 프로젝트, 2018/05/15, 신혜민(B889041) #

players = '안나', '신후', '유나', '원준'

schedule = set()

for a in players:
    for b in players:
        if a!=b:
            schedule.add((a, b))

print(schedule)

new_schedule = [(a, b) for a in players for b in players if a !=b]

print(new_schedule)
