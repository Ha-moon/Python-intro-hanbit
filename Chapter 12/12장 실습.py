# 12장 실습 프로젝트, 2018/06/05, 신혜민(B889041) #

def print_baggage_items(*items, **item_with_count):

    print('# 단일 품목')
    for a in items:
        print(a)
        
    print('\n# 다중 품목')
    for b in item_with_count.keys():
        print(b, item_with_count[b],'개')

print_baggage_items('laptop', 'camera','charger',socks=8, pants=2, shirts=4)
