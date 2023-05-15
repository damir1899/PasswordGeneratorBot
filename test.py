from string import ascii_letters
import random

def password_generator(number):
    all_letters = list(ascii_letters)
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    all_letters.extend(numbers)
    password = ''
    for i in range(1, int(number)+1):
        word = str(random.choice(all_letters))
        password += word
    return password

print(password_generator(5))