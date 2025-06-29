# Import dependencies
from art import logo, vs
from game_data import data
import random

# Display ascii art
print(logo)

# Function 'comparison_a()' gets a random value from list 'data', then returns the follower_count element from value
def comparison_a():
    random_compare_a = random.choice(data)
    print(f"Compare A: {random_compare_a['name']}, a {random_compare_a['description']}, from {random_compare_a['country']}")
    return random_compare_a['follower_count']

# Function 'comparison_b()' gets a random value from list 'data', then returns the follower_count element from value
def comparison_b():
    random_compare_b = random.choice(data)
    print(f"Compare B: {random_compare_b['name']}, a {random_compare_b['description']}, from {random_compare_b['country']}")
    return random_compare_b['follower_count']

# Score counter
score = 0
# Create Boolean value (True) that ends while loop when False
continue_game = True

while continue_game:
    a = comparison_a()
    print(vs)
    b = comparison_b()
    guess_followers = input(f"Who has more followers? Type 'A' or 'B': ").upper()
    print("\n" * 20)

    if guess_followers == 'A' and a > b:
        score += 1
        print(f"You're right! Current score: {score}")
    if guess_followers == 'A' and a < b:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False
    if guess_followers == 'B' and b > a:
        score += 1
        print(f"You're right! Current score: {score}")
    if guess_followers == 'B' and b < a:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False
