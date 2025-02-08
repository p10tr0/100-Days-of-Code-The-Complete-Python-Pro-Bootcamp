import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    print(art.logo)
    # Creates a deal_card() function that uses the list below to return a random card
    def deal_card():
        # Returns a random card from the deck
        card = random.choice(cards)
        return card
    # Creates a compare_scores() function to check the scores.
    def compare_scores(u_score, c_score):
        if u_score == c_score:
            return "The game is a draw."
        elif c_score == 0:
            return "You lose, Computer has Blackjack."
        elif u_score == 0:
            return "You win with a Blackjack."
        elif u_score > 21:
            return "You lose, you went over 21."
        elif c_score > 21:
            return "Computer went over, You win."
        elif u_score > c_score:
            return "You win."
        else:
            return "You lose."

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    # Deal the user and computer two cards using deal_card() and append()
    for value in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Creates a function called calculate_score() that takes a list of cards as input and returns the sum of all the cards in the list as the score.
    def calculate_score(cards_to_check):
        # Check for a blackjack (2 cards: ace + 10) and return 0 instead of the actual score. 0 represents a blackjack
        if 11 in cards_to_check and 10 in cards_to_check and len(cards_to_check) == 2:
            return 0

        # Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
        if 11 in cards_to_check and sum(cards_to_check) > 21:
            cards_to_check.remove(11)
            cards_to_check.append(1)

        return sum(cards_to_check)

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computers first card: {computer_cards[0]}")

        # Call the calculate_score() functions. If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            # If the game has not ended, ask the user if they want to draw another card. If yes, use deal_card() to add another card to the user_cards() list. If no, then the game has ended.
            draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_another_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Users final hand: {user_cards}, final score: {user_score}")
    print(f"Computers final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)
    blackjack()
