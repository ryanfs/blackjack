import random

# deck = {
# 	'2 of Spades' : 2,
# 	 '3 of Spades' : 3,
# 	 '4 of Spades' : 4,
# 	 '5 of Spades' : 5,
# 	 '6 of Spades' : 6,
# 	 '7 of Spades' : 7,
# 	 '8 of Spades' : 8,
# 	 '9 of Spades' : 9,
# 	 '10 of Spades' : 10,
# 	 'Jack of Spades' : 10,
# 	 'Queen of Spades' : 10,
# 	 'King of Spades' : 10,
# 	 'Ace of Spades' : 1,
# 	 '2 of Hearts' : 2,
# 	 '3 of Hearts' : 3,
# 	 '4 of Hearts' : 4,
# 	 '5 of Hearts' : 5,
# 	 '6 of Hearts' : 6,
# 	 '7 of Hearts' : 7,
# 	 '8 of Hearts' : 8,
# 	 '9 of Hearts' : 9,
# 	 '10 of Hearts' : 10,
# 	 'Jack of Hearts' : 10,
# 	 'Queen of Hearts' : 10,
# 	 'King of Hearts' : 10,
# 	 'Ace of Hearts' : 1,
# 	 '2 of Clubs' : 2,
# 	 '3 of Clubs' : 3,
# 	 '4 of Clubs' : 4,
# 	 '5 of Clubs' : 5,
# 	 '6 of Clubs' : 6,
# 	 '7 of Clubs' : 7,
# 	 '8 of Clubs' : 8,
# 	 '9 of Clubs' : 9,
# 	 '10 of Clubs' : 10,
# 	 'Jack of Clubs' : 10,
# 	 'Queen of Clubs' : 10,
# 	 'King of Clubs' : 10,
# 	 'Ace of Clubs' : 1,
# 	 '2 of Diamonds' : 2,
# 	 '3 of Diamonds' : 3,
# 	 '4 of Diamonds' : 4,
# 	 '5 of Diamonds' : 5,
# 	 '6 of Diamonds' : 6,
# 	 '7 of Diamonds' : 7,
# 	 '8 of Diamonds' : 8,
# 	 '9 of Diamonds' : 9,
# 	 '10 of Diamonds' : 10,
# 	 'Jack of Diamonds' : 10,
# 	 'Queen of Diamonds' : 10,
# 	 'King of Diamonds' : 10,
# 	 'Ace of Diamonds' : 1
# }

#test deck
deck = {
	 '8 of Spades' : 8,
	 '9 of Spades' : 9,
	 '10 of Spades' : 10,
	 'Ace of Spades' : 1,
	 '9 of Hearts' : 9,
	 'Ace of Hearts' : 1,
	 'Jack of Clubs' : 10,
	 'Queen of Clubs' : 10,
	 'King of Clubs' : 10,
	 'Ace of Clubs' : 1,
	 'Ace of Diamonds' : 1
}

def shuffle_the_deck():
	cards = deck.keys()
	random.shuffle(cards)
	return cards

def deal(cards):
	my_hand = []
	while len(my_hand) <= 1:
		dealtCard = cards.pop(0)
		my_hand.append(dealtCard)
	print "You have: "
	for card in my_hand:
		print card
	return my_hand

def deal_to_dealer(cards):
	house_hand = []
	while len(house_hand) <= 1:
		dealtCard = cards.pop(0)
		house_hand.append(dealtCard)
	print "Dealer is showing: ", house_hand[1]
	#print "(By the way the dealer has %s)" % house_hand
	return house_hand


def get_numerical_value(hand):
	val = 0
	for card in hand:
		val += deck[card]
	return val

# def get_numerical_value(hand):
# 	sum = 0
# 	ace = False
# 	for card in hand:
# 		sum += deck[card]
# 		if card == 'Ace of Spades' or 'Ace of Clubs' or 'Ace of Hearts' or 'Ace of Diamonds':
# 			ace = True
# 	if ace and sum  <= 11:
# 		return sum + 10
# 	else:
# 		return sum


def compare_hands(my_hand, house_hand):
 	player_value_of_hand = get_numerical_value(my_hand)
 	dealer_value_of_hand = get_numerical_value(house_hand)
	if get_numerical_value(my_hand) > get_numerical_value(house_hand):
		print "You ended with %d and the dealer ended with %d" % (player_value_of_hand, dealer_value_of_hand)
		print "You win! Hurray! Gambling rules!"
	elif get_numerical_value(my_hand) == get_numerical_value(house_hand):
		print "Push... Whatever."
	else:
		print "You have %d and the House has %d" % (player_value_of_hand, dealer_value_of_hand)
		print "Sorry, the House wins. The House always wins..."

def hit(hand, cards, house_hand):
	dealtCard = cards.pop(0)
	hand.append(dealtCard)
	print "You've chosen to hit, now your cards are:"
	for card in hand:
		print card
	my_hand = get_numerical_value(hand)
	if my_hand > 21:
		print "Oh no... %d! Too much! Bust." % my_hand
		exit()

	elif my_hand == 21:
		print "Alright, you've got 21! Let's see what the dealer has..."
		compare_hands(hand, house_hand)
	else:
		print "Now you have a total of %d" % my_hand
		print "Your move again"
		move = raw_input("would you like to hit or stay? (hit / stay)")
		newChoice = hit_or_stay(move, hand, house_hand, cards)
	return my_hand

def dealer_hit_or_stay(house_hand, cards, my_hand):
	dealer_value = get_numerical_value(house_hand)
	if dealer_value < 17:
		while dealer_value < 17:
			print "Dealer has %d" % dealer_value
			dealtCard = cards.pop(0)
			print "Let's flip the dealer's cards over: %s" % house_hand
			house_hand.append(dealtCard)
			print "That's less than 17 so the dealer will take a hit and now has %s " % house_hand
			dealer_value = get_numerical_value(house_hand)
		return dealer_value
		return house_hand
	elif dealer_value <= 21: 
		print "Dealer cards: ", house_hand
		print "Dealer stays. Let's compare our hands."
		compare_hands(my_hand, house_hand)
	else:
		print "Dealer busts with %d! You win!" % dealer_value
		exit()
	return dealer_value

def hit_or_stay(move, my_hand, house_hand, cards):
	if move == "hit":
		hit(my_hand, cards, house_hand)

	elif move == "stay":
		print "You've chosen to stay. Let's see the dealer's cards."
		dealer_hit_or_stay(house_hand, cards, my_hand)
	else:
		print "You didn't do hit or stay. C'mon man..."


def playRound(cards):
	my_hand = deal(cards)
	house_hand = deal_to_dealer(cards)
	dealer_value = get_numerical_value(house_hand)
	move = raw_input("would you like to hit or stay? (hit / stay)")
	my_choice = hit_or_stay(move, my_hand, house_hand, cards)
	value_of_my_hand = get_numerical_value(my_hand)
	print "value of my hand is now: ", value_of_my_hand
	#newHouse = dealer_hit_or_stay(house_hand, cards, my_hand)
	compare_hands(my_hand, house_hand)

	return my_hand, house_hand, value_of_my_hand, dealer_value, move, my_choice

def run():
	cards = shuffle_the_deck()
	my_hand, house_hand, value_of_my_hand, dealer_value, move, my_choice = playRound(cards)

	
	
	#work on this hit or stay function, get it to work... 

if __name__ == '__main__':
	run()