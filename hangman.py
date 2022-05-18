from keyword import iskeyword
import random

def is_letter(userInput):
    isLetter = userInput.isalpha()
    if isLetter:
        return True
    return False

def is_valid_level(difficulty):
    if difficulty == "łatwy" or difficulty == "średni" or difficulty == "trudny":
        return True
    return False

def ask_for_letter(force_valid_input):
    while True:
        letter = input("Podaj literę:")
        isLetter = is_letter(letter)
        if isLetter is False:
            if not force_valid_input:
                return None
            print("Nie właściwy znak")
        else:
            return letter
    
def check_letter(letter):
    small_letter = letter.lower()
    while True:
        if small_letter == "quit":
            quit()
        if len(small_letter) > 1:
            small_letter = input("Wybierz tylko 1 literę:")
        else:
            return small_letter

def check_tried_letters(letter, tried_letters):
    if len(tried_letters) == 0 or letter not in tried_letters:
        tried_letters.append(letter)
    else:
        while letter in tried_letters and len(tried_letters) >= 1:
            letter = input("Litera została już wybrana, wybierz inną:")
        tried_letters.append(letter)
    return tried_letters
            
def current_word(country, tried_letters, char, current):
    for i in range(0,len(country)):
        if country[i] == char.upper():
            tried_letters.append(char.upper())
        if country[i] == char:
            current[i] = char
        elif country[i] == char.upper():
            current[i] = char.upper()
        """elif country[i] == tried_letters[-1]:
            current[i] = tried_letters[-1]"""
    return "".join(current).rstrip()

def display_hangman(count, image):
    print(image[0 + count])

def set_lives(lives, level):
    if level == "łatwy":
        lives = 8
    elif level == "średni":
        lives = 6
    elif level == "trudny":
        lives = 4
    print("Masz obecnie %d żyć: " % lives)
    return lives

def set_difficulty(level, image):
    if level == "średni":
        image = image[2:]
    elif level == "trudny":
        image = image[4:]
    return image

def hidden_word(country):
    #print(slowo)
    if " " in country:
        hidden = ""
        hidden_words = country.split(" ")
        for char in hidden_words:
            hidden += "_"*len(char) + " "
    else:
        hidden = "_"*len(country)
    print(hidden + "\n")
    return hidden

def ask_for_difficulty(force_valid_input):
    while True:
        difficulty = input("Wybierz poziom: łatwy, średni, trudny:")
        isValid = is_valid_level(difficulty)
        if isValid is False:
            if not force_valid_input:
                return None
            print("Wpisałeś niezrozumiałą komendę")
        else:
            return difficulty

def read_from_file():
    list = []

    with open('countries.txt') as f:
        for line in f:
            list.append(line.split(" | ", 1)[0])
    return list

def generate_guess():
    countries = read_from_file()
    return random.choice(countries)

def status(result, lives, country):
    if result == country:
        return False
    elif lives == 0:
        print("Przegrałeś")
        return False
    return True


def hangman():
    result = ""
    count = 0
    already_tried_letters = []
    
    HANGMANPICS = [
    "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
    
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

    "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

    "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

    "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="
    ]  
    
    level = ask_for_difficulty(True)
    lives = set_lives(0, level)
    art = set_difficulty(level, HANGMANPICS)
    country = generate_guess()
    print("Zgadnij, który to kraj w języku angielskim")
    hidden = hidden_word(country)
    current = list(hidden)
    letter = ask_for_letter(True)
    char = check_letter(letter)
    tried_letters = check_tried_letters(char, already_tried_letters)
    check_status = status(result, lives, country)

    while check_status != False:
        char = tried_letters[-1]
        if char.lower() not in country.lower():
            lives -= 1
            display_hangman(count, art)
            count += 1
            print("Nie zgadłeś, masz obecnie: %d żyć" % lives)
        result = current_word(country, tried_letters, char, current)
        print(result + "\n")
        check_status = status(result, lives, country)
        if check_status != False:
            letter = ask_for_letter(True)
            char = check_letter(letter)
            tried_letters = check_tried_letters(char, already_tried_letters)

    if check_status == False and lives > 0:
        print("Gratulacje, zgadłeś!")

if __name__ == '__main__':
    hangman()
