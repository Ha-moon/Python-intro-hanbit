Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #339p
>>> cards = [(color, number) for color in ('R','B','G','Y') for number in range(10)]
>>> cards
[('R', 0), ('R', 1), ('R', 2), ('R', 3), ('R', 4), ('R', 5), ('R', 6), ('R', 7), ('R', 8), ('R', 9), ('B', 0), ('B', 1), ('B', 2), ('B', 3), ('B', 4), ('B', 5), ('B', 6), ('B', 7), ('B', 8), ('B', 9), ('G', 0), ('G', 1), ('G', 2), ('G', 3), ('G', 4), ('G', 5), ('G', 6), ('G', 7), ('G', 8), ('G', 9), ('Y', 0), ('Y', 1), ('Y', 2), ('Y', 3), ('Y', 4), ('Y', 5), ('Y', 6), ('Y', 7), ('Y', 8), ('Y', 9)]
>>> 
>>> new_cards = list()
>>> import random
>>> while len(cards) > 0:
	new_cards.append(cards.pop(random.randint(0, len(cards)-1)))

	
>>> new_cards
[('Y', 0), ('B', 7), ('G', 4), ('B', 8), ('G', 2), ('R', 6), ('R', 3), ('Y', 4), ('Y', 8), ('R', 4), ('B', 1), ('B', 0), ('R', 1), ('G', 8), ('G', 9), ('G', 1), ('Y', 2), ('Y', 3), ('B', 2), ('R', 2), ('Y', 5), ('Y', 6), ('G', 0), ('R', 8), ('B', 5), ('R', 5), ('Y', 1), ('R', 7), ('B', 9), ('G', 7), ('G', 3), ('R', 0), ('B', 3), ('G', 5), ('Y', 9), ('G', 6), ('B', 4), ('R', 9), ('B', 6), ('Y', 7)]
>>> 
>>> 
>>> #340p
>>> computer_cards = list()
>>> human_cards = list()
>>> for index in range(7):
	computer_cards.append(new_cards.pop())
	human_cards.append(new_cards.pop())

	
>>> computer_cards
[('Y', 7), ('R', 9), ('G', 6), ('G', 5), ('R', 0), ('G', 7), ('R', 7)]
>>> human_cards
[('B', 6), ('B', 4), ('Y', 9), ('B', 3), ('G', 3), ('B', 9), ('Y', 1)]
>>> new_cards
[('Y', 0), ('B', 7), ('G', 4), ('B', 8), ('G', 2), ('R', 6), ('R', 3), ('Y', 4), ('Y', 8), ('R', 4), ('B', 1), ('B', 0), ('R', 1), ('G', 8), ('G', 9), ('G', 1), ('Y', 2), ('Y', 3), ('B', 2), ('R', 2), ('Y', 5), ('Y', 6), ('G', 0), ('R', 8), ('B', 5), ('R', 5)]
>>> 
>>> #341p
>>> used_cards = list()
>>> board_card = new_cards.pop()
>>> used_cards.append(board_card)
>>> board_card
('R', 5)
>>> used_cards
[('R', 5)]
>>> 
>>> #342p
>>> def check_cards_status_and_reset(current, used):
	if len(current) == 0:
		used_index = len(used) - 1
		while used_index >= 0:
			current.append(used[used_index])
			used_index -= 1
		used.clear()
	return current

>>> 
>>> #343p
>>> def pop_new_card(current, used):
	check_cards_status_and_reset(current, used)
	return current.pop()

>>> 
>>> def find_match_card(player, board_card, player_cards, new_cards, used_cards):
	print('현재 보드 카드 :', board_card, '[', player[0:3], ']의 카드 세트 :', player_cards)
	has_match = False
	for card in player_cards:
		if card[0] == board_card[0] or card[1] == board_card[1]:
			player_cards.remove(card)
			used_cards.append(card)
			has_match = True
			return card
		if has_match == False:
			player_cards.append(pop_new_card(new_cards, used_cards))
			return board_card

		
>>> 
>>> #345p
>>> board_card = find_match_card('COMPUTER', board_card, computer_cards, new_cards, used_cards)
현재 보드 카드 : ('R', 5) [ COM ]의 카드 세트 : [('Y', 7), ('R', 9), ('G', 6), ('G', 5), ('R', 0), ('G', 7), ('R', 7)]
>>> board_card
('R', 5)
>>> computer_cards
[('Y', 7), ('R', 9), ('G', 6), ('G', 5), ('R', 0), ('G', 7), ('R', 7), ('B', 5)]
>>> used_cards
[('R', 5)]
>>> 
>>> #346p
>>> board_card = find_match_card('HUMAN', board_card, human_cards, new_cards, used_cards)
현재 보드 카드 : ('R', 5) [ HUM ]의 카드 세트 : [('B', 6), ('B', 4), ('Y', 9), ('B', 3), ('G', 3), ('B', 9), ('Y', 1)]
>>> board_card
('R', 5)
>>> human_cards
[('B', 6), ('B', 4), ('Y', 9), ('B', 3), ('G', 3), ('B', 9), ('Y', 1), ('R', 8)]
>>> used_cards
[('R', 5)]
>>> 
>>> #347p
>>> if len(computer_cards) == 0:
	print('COMPUTER WIN !! ')
	break
SyntaxError: 'break' outside loop
>>> if len(computer_cards) == 0:
	print('COMPUTER WIN !! ')
	break
SyntaxError: 'break' outside loop
>>> 
