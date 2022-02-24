import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)


def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2: # blackjack
        return 0
    elif score > 21 and 11 in cards:
        print("Now counting ace as 1 and not 11")
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


def compare(user_score, computer_score):
    if user_score == 0:
        user_score = 'Blackjack'

    if computer_score == 0:
        computer_score = 'Blackjack'

    print(f"Your score: {user_score}. Your cards: {user_cards} -- computer score: {computer_score}. Computer cards: {computer_cards}")
    if user_score == computer_score or (user_score > 21 and computer_score > 21):
        print("It's a draw")
    elif computer_score == 'Blackjack':
        print("The computer wins!")
    elif user_score == 'Blackjack':
        print("You win!")
    elif user_score > 21:
        print("Bust! You lose")
    elif computer_score > 21:
        print("Computer is bust! You win")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("You lose!")


user_cards = []
computer_cards = []

for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

while user_score != 0 and computer_score != 0 and user_score <= 21:
    print(user_cards)
    print(user_score)
    another = input("Draw another card? (y/n) ").casefold()
    if another == 'n' or another == 'no':
        break
    user_cards.append(deal_card())
    user_score = calculate_score(user_cards)

while computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)


compare(user_score, computer_score)