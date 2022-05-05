from keyword import iskeyword
import random
from sys import stdout

def is_letter(userInput):
    isLetter = userInput.isalpha()
    if isLetter:
        return True
    else:
        return False

def is_valid_level(poziom):
    if poziom == "łatwy" or poziom == "średni" or poziom == "trudny":
        return True
    return False

def ask_for_letter(force_valid_input):
    while True:
        litera = input("Podaj literę:")
        czy_litera = is_letter(litera)
        if czy_litera is False:
            if not force_valid_input:
                return None
            print("Nie właściwy znak")
        else:
            return litera
        pass
    
def check_letter(litera):
    malyZnak = litera.lower()
    while True:
        if malyZnak == "quit":
            quit()
        if len(malyZnak) != 1:
            malyZnak = input("Wybierz tylko 1 literę:")
        else:
            return malyZnak

def check_tried_letters(litera, tried_letters):
    if len(tried_letters) == 0 or litera not in tried_letters:
        tried_letters.append(litera)
    else:
        while litera in tried_letters and len(tried_letters) >= 1:
            litera = input("Litera została już wybrana, wybierz inną:")
    return tried_letters
            
def current_word(slowo, tried_letters, checking):
    if slowo[0] == checking.upper():
        tried_letters.append(checking.upper())
    current_word = "".join(x if x in tried_letters else '_' for x in slowo)
    return current_word

def life_decreases(lives):
    lives -= 1
    return lives

def display_hangman(count, lives, image):
    print(image[0 + count])
    print("Nie zgadłeś, masz obecnie: %d żyć" % lives)

def set_lives(zycie, level):
    if level == "łatwy":
        zycie = 8
    elif level == "średni":
        zycie = 6
    elif level == "trudny":
        zycie = 4
    print("Masz obecnie %d żyć: " % zycie)
    return zycie

def set_difficulty(level, image):
    if level == "średni":
        image = image[2:]
    elif level == "trudny":
        image = image[4:]
    return image

def hidden_word(slowo):
    print(slowo)
    zagadka = "_"*len(slowo)
    print(zagadka)

def ask_for_difficulty(force_valid_input):
    while True:
        poziom = input("Wybierz poziom: łatwy, średni, trudny:")
        isValid = is_valid_level(poziom)
        if isValid is False:
            if not force_valid_input:
                return None
            print("Wpisałeś niezrozumiałę komendę")
        else:
            return poziom

def read_from_file():
    lista = []

    with open('countries.txt') as f:
        for line in f:
            lista.append(line.split(" | ", 1)[0])
    return lista

def generate_guess():
    countries = read_from_file()
    return random.choice(countries)

def status(result, lives):
    if result.isalpha():
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
    slowo = generate_guess()
    hidden_word(slowo)
    litera = ask_for_letter(True)
    char = check_letter(litera)
    tried_letters = check_tried_letters(char, already_tried_letters)
    check_status = status(result, lives)

    while check_status != False:
        if char.lower() not in slowo.lower():
            lives = lives - 1
            display_hangman(count, lives, art)
            count += 1     
        result = current_word(slowo, tried_letters, char)
        print(result)
        check_status = status(result, lives)
        if check_status != False:
            litera = ask_for_letter(True)
            char = check_letter(litera)
            tried_letters = check_tried_letters(char, already_tried_letters)

    if check_status == False and lives > 0:
        print("Gratulacje, zgadłeś!")

if __name__ == '__main__':
    hangman()
