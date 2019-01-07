# 10장 심화 프로젝트II, 2018/05/15, 신혜민(B889041) #

books=[]

books.append({'제목': '개발자의 코드', '출판연도':'2013.02.28', '출판사': 'A', '쪽수': 200, '추천유무': False})
books.append({'제목': '클린 코드', '출판연도':'2013.03.04', '출판사': 'B', '쪽수': 584, '추천유무': True})
books.append({'제목': '빅데이터 마케팅', '출판연도':'2014.07.02', '출판사': 'A', '쪽수': 296, '추천유무': True})
books.append({'제목': '구글드', '출판연도':'2010.02.10', '출판사': 'B', '쪽수': 526, '추천유무': False})
books.append({'제목': '강의력', '출판연도':'2013.12.12', '출판사': 'A', '쪽수': 248, '추천유무': True})

print('전체 책 목록')

many_page=[]
recommends=[]
all_pages=0
pub_company=set()


for x in books:
    print(x)
    if x['쪽수']>250:
        many_page.append(x['제목'])
    if x['추천유무']==True:
        recommends.append(x['제목'])
    all_pages=all_pages+x['쪽수']
    pub_company.add(x['출판사'])
    
print('\n\n쪽수가 250 쪽 넘는 책 리스트:', many_page)
print('내가 추천하는 책 리스트:', recommends)
print('내가 읽은 책 전체 쪽수:', all_pages)
print('내가 읽은 책의 출판사 목록:', pub_company)

new_page=[x['제목'] for x in books if x['쪽수']>250]
print('\n한 줄로 만든 쪽수가 250쪽 넘는 책 리스트 : ', many_page)
