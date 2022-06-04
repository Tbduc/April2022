import re, string

def clean(text):
    text = "".join(c for c in text if c.isalpha())
    return text

def is_palindrome(str):
    str = clean(str)
    n = len(str)
    for i in range(0, int(n/2)):
        if str[i].lower() != str[len(str) - i -1].lower():
            return False
    return True
                

print(is_palindrome("Kobyła ma mały bok"))
print(is_palindrome("Mama") == False)

def is_isogram(text):
    text = clean(text)
    repeated_letter_list = []
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if(text[i].lower() == text[j].lower()):
                repeated_letter_list.append(text[i])
                if(len(repeated_letter_list) > 1):
                    return False
    return True

print(is_isogram("Country is b") == True)
print(is_isogram("Country is b, ") == True)

def is_pangram(text):
    alphabet = string.ascii_lowercase
    text = clean(text)
    for letter in alphabet:
        if letter not in text:
            return False
    return True
    
print(is_pangram("Sphinx of black quartz, judge my vow") == True)
print(is_pangram("Sphinx of order quartz, judge my vow") == False)

def is_anagram(text, text2):
    text = clean(text)
    text2 = clean(text2)
    letter_list1= []
    letter_list2= []
    for i in range(len(text)):
        letter_list1.append(text[i])
        for j in range(len(text2)):
            letter_list2.append(text2[j])
    if letter_list1.sort() == letter_list2.sort():
        return True
    return False

is_anagram("eleven plus two", "twelve plus one")

def is_pangram(text):
    alphabet = string.ascii_lowercase
    text = clean(text)
    for letter in alphabet:
        if letter not in text:
            return False
    return True
    
print(is_pangram("Sphinx of black quartz, judge my vow") == True)
print(is_pangram("Sphinx of order quartz, judge my vow") == False)

def is_anagram2(text, text2):
    text = clean(text)
    text2 = clean(text2)
    
    return sorted(text) == sorted(text2)

is_anagram2("eleven plus two", "twelve plus one")