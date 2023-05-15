import random
from string import ascii_letters


def password_generator(number):
    number = int(number)
    all_letters = list(ascii_letters)
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    all_letters.extend(numbers)
    passw = ''
    
    for i in range(1, int(number)+1):
        if len(passw) == number:
            break
        word = str(random.choice(all_letters))
        passw += word
        
    return passw