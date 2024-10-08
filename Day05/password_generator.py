import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Empty list to store the random password characters
character_list = []

# For loop to loop through the number of selected letters
for letter in range(nr_letters):
    random_letter = random.choice(letters)
    character_list.append(random_letter)

# For loop to loop through the number of selected symbols
for symbol in range(nr_symbols):
    random_symbol = random.choice(symbols)
    character_list.append(random_symbol)

# For loop to loop through the number of selected numbers
for number in range(nr_numbers):
    random_number = random.choice(numbers)
    character_list.append(random_number)

# Randomise the elements within character_list using the shuffle() method
random.shuffle(character_list)

# Print a random list of password characters, and use .join() method to join character_list elements
print(f"Your password is: {''.join(character_list)}")