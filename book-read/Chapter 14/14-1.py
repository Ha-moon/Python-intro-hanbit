import random  # random 모듈 탑재

# 카드 세트의 상태를 확인하여 비었으면 사용한 카드 세트를 다시 사용하는 함수
def check_cards_status_and_reset(current, used):
        if len(current) == 0:
            used_index = len(used) - 1
            while used_index >= 0:
                current.append(used[used_index])
                used_index -= 1
            used.clear()
            
        return current

# 카드 세트에서 신규 카드를 추출한다.
def pop_new_card(current, used):
    
    # 카드 세트의 상태 확인하여 처리
    check_cards_status_and_reset(current, used)

    # 현재 카드 세트에서 카드 하나를 추출하여 반환
    return current.pop()

# 조건에 맞는 카드 유무를 확인하여 처리하는 함수
def find_match_card(player, board_card, player_cards, new_cards, used_cards):

    # 현재 플레이어 현황 출력
    print('현재 보드 카드 :', board_card, '[', player[0:3], ']의 카드 세트 :', player_cards)
    
    # 조건에 맞는 카드 유무 확인을 위한 플래그
    has_match = False

    # 플레이어 카드 확인
    for card in player_cards:
        
        # 색이 같거나 숫자가 같으면 낼 수 있다.
        if card[0] == board_card[0] or card[1] == board_card[1]:

            # 플레이어 카드 세트에서 제거
            player_cards.remove(card)

            # 사용한 카드 세트에 추가
            used_cards.append(card)

            # 플래그 변경
            has_match = True
            
            # 보드 카드 변경을 위해 카드 반환
            return card

    # 만약 조건에 맞는 카드가 없다면 플레이어 카드 세트에 카드를 추가한다.
    if has_match == False:
        
        # 플레이어 카드 세트에 신규 카드 추가
        player_cards.append(pop_new_card(new_cards, used_cards))

        # 보드 카드는 변경되지 않았으니, 인수로 받은 보드 카드 반환
        return board_card


def logging_all(cards, coms, hums, used):
    print('### 현황판 >>> [NEW :', len(cards), '] [COM :', len(coms), '] [HUM :', len(hums), '] [USED :', len(used), ']')
    
class CardGame:

    # 카드 게임 초기화 함수
    def __init__(self):
        
        # 플레이어 카드 개수 초기화
        self.player_card_count = 7

        # 게임 준비
        self.prepare_game()

    # 카드 게임을 시작하기 위한 준비
    def prepare_game(self):
        
        # 기본 카드 세트 생성
        self.cards = [(color, number) for color in ('R','B','G','Y') for number in range(10)]

        # 신규 카드 세트를 위한 리스트 생성
        self.new_cards = list()

        # 기본 카드 세트에서 임의 추출하여 신규 카드 생성
        while len(self.cards) > 0:
            self.new_cards.append(self.cards.pop(random.randint(0, len(self.cards)-1)))
    
        # 각 플레이어 카드 세트를 우한 리스트 초기화
        self.computer_cards = list()
        self.human_cards = list()

        # 각 플레이어에게 카드 할당
        for index in range(self.player_card_count):
            self.computer_cards.append(self.new_cards.pop())
            self.human_cards.append(self.new_cards.pop())

        # 게임 준비 완료 메시지 출력
        print('== 카드 게임을 위한 준비가 모두 끝났습니다. =================================')
        print('컴퓨터 :', self.computer_cards)
        print('사   람 :', self.human_cards)

    # 카드 게임 자동 버전 play 함수
    def play_auto_game(self):

        # 사용한 카드 세트 초기화
        self.used_cards = list()

        # 현황판 출력
        logging_all(self.new_cards, self.computer_cards, self.human_cards, self.used_cards)

        # 보드 카드 초기 세팅
        self.board_card = self.new_cards.pop()

        # 사용한 카드에 초기 보드 카드 추가
        self.used_cards.append(self.board_card)

        # 게임 라운드 회수 저장을 위한 변수 선언
        round_count = 0

        # 각 플레이어가 카드를 가지고 있는 동안 반복한다.
        while len(self.computer_cards) > 0 and len(self.human_cards) > 0:

            # 라운드 표기
            print('\n== ROUND', round_count, '===================================')

            # 신규 카드 세트의 상태를 확인한다. 비었으면 사용한 카드를 채워 넣는다.
            check_cards_status_and_reset(self.new_cards, self.used_cards)

            # 컴퓨터의 카드 중 제거할 수 있는 카드가 있는지 확인한다. 있으면 그 카드가 보드 카드가 된다.
            self.board_card = find_match_card('COMPUTER', self.board_card, self.computer_cards, self.new_cards, self.used_cards)

            # 컴퓨터의 카드를 다 쓰면 컴퓨터가 승리한다.
            if len(self.computer_cards) == 0:
                print('COMPUTER WIN !! ')
                break     # 상위 while 문 탈출
            
            # 사람의 카드 중 제거할 수 있는 카드가 있는지 확인한다. 있으면 그 카드가 보드 카드가 된다.
            self.board_card = find_match_card('HUMAN', self.board_card, self.human_cards, self.new_cards, self.used_cards)

            # 사람의 카드를 다 쓰면 컴퓨터가 승리한다.
            if len(self.human_cards) == 0:
                print('HUMAN WIN !! ')
                break     # 상위 while 문 탈출

            # 현황판 출력
            logging_all(self.new_cards, self.computer_cards, self.human_cards, self.used_cards)

            # 라운드 카운트 증가
            round_count += 1

# 카드 게임 실행
CardGame().play_auto_game()
