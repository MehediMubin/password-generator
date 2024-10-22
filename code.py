import random
import string

def generate_password(min_length, contains_numbers, contains_symbols):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    characters = letters
    if contains_numbers:
        characters += numbers
    if contains_symbols:
        characters += symbols

    password = ''
    meets_criteria = False
    has_number = False
    has_symbol = False

    while not meets_criteria or len(password) < min_length:
        new_character = random.choice(characters)
        password += new_character

        if new_character in numbers:
            has_number = True
        elif new_character in symbols:
            has_symbol = True

        meets_criteria = True
        if contains_numbers:
            meets_criteria = has_number
        if contains_symbols:
            meets_criteria = meets_criteria and has_symbol

    return password

password_length = input('Please give a minimum password length: ')
if not password_length.isdigit():
    print('Invalid password length')
else:
    password_length = int(password_length)
    number_exists = input('Do you want to have numbers? (y/n): ').lower() == 'y'
    symbol_exists = input('Do you want to have symbols? (y/n): ').lower() == 'y'
    generated_password = generate_password(password_length, number_exists, symbol_exists)

    print(generated_password)