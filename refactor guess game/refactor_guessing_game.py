import random
from config.config import MAX_RANDOM_NUMBER, MIN_RANDOM_NUMBER

def get_random_number(nim_number: int, max_number: int) -> int:
    """
    Generetas rundom number from particular range
 
    Returns: int -> random number
    """
    return random.randint(int(nim_number),int(max_number)) 
 
 
def game(count: int, min_number: int, max_number: int):
    """
    Runs entire game flow 
 
    Args:
      count: int -> how many tims game is invoked
      min_number: int -> min number that can be randomly selected
      max_number: int -> max number that can be randomly selected
    """
    for i in range(count):
        random_number = get_random_number(min_number, max_number)
        guess_number = int(input(f"Enter an integer from {min_number} to {max_number}: "))
        while random_number != guess_number:
            if guess_number < random_number:
                print("guess is low")
            elif guess_number > random_number:
                print("guess is high")
            guess_number = int(input(f"Enter an integer from {min_number} to {max_number}: ")) 
        print("you guessed it!")

def generate_random_list(el_number: int, MIN_RANDOM_NUMBER: int, MAX_RANDOM_NUMBER: int):
    l = []
    for i in range(el_number):
        l.append(random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER))
    return l

def game2(random_list):
    """
    Runs entire game flow 

    Args:
      count: int -> how many tims game is invoked
      min_number: int -> min number that can be randomly selected
      max_number: int -> max number that can be randomly selected
    """
    for random_number in random_list:
        guess_number = int(input(f"Enter an integer from min to max"))
        while random_number != guess_number:
            if guess_number < random_number:
                print("guess is low")
            elif guess_number > random_number:
                print("guess is high")
            guess_number = int(input(f"Enter an integer from min to max")) 
        print("you guessed it!")

 
if __name__ == '__main__':
    game2(10, 1, 30)