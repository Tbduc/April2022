from random import *
import math
def is_number(userInput):
    number = str(userInput)
    if number.strip().lstrip('-').replace('.', '', 1).isdigit():
        return True
    else:
        return False
    pass

def convert_number(str):
    intNumber = int(str)
    return intNumber
    pass

def ask_for_lower_bound(force_valid_input):
    while True:
        a = input("Select lower bound:")
        a_number = is_number(a)
        if a_number is False:
            if not force_valid_input:
                return None
            print("Incorrect input")
        else:
            return convert_number(a)
        pass
    
def ask_for_upper_bound(force_valid_input):
    while True:   
        b = input("Select upper bound:")
        b_number = is_number(b)
        if b_number is False:
            if not force_valid_input:
                return None
            print("Incorrect input")
        else:
            return convert_number(b)
        pass


def guess_a_number(force_valid_input):
    while True:
        number = input("Guess a number:")
        isValid = is_number(number)
        
        if isValid is False:
            if not force_valid_input:
                return None
            print("Incorrect number")
        else:
            return convert_number(number)
        pass

def generate_random_number(a, b):
    randomNumber = randint(a, b)
    print("\n\tYou've only ",
       round(math.log(b - a + 1, 2)),
      " chances to guess the integer!\n")
    return randomNumber
    pass

def checking(lower, upper, number, randomNumber):
    if not is_number(lower) or not is_number(upper) or not is_number(number):
        return None
    elif number == randomNumber:
        print("Congratulations!")
        return False
    elif number < randomNumber:
        print("Try Again! You guessed too small.")
    elif number > randomNumber:
        print("Try Again! You guessed too high.")
        
    return True
    pass
      
def guessing_game():
    a = ask_for_lower_bound(True)
    b = ask_for_upper_bound(True)
    x = generate_random_number(a, b)
    guesses = round(math.log(b - a + 1, 2))
    c = guess_a_number(True)
    counter = 1
    while checking(a, b, c, x):
        c = guess_a_number(True)
        counter += 1
        if checking is not False and counter == guesses:
            print("Better Luck Next Time!")
            break
    pass
    
if __name__ == '__main__':
    guessing_game()