from calendar import month_abbr
import imp


import random

ALL_MONTHS = ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]

'''
Your friend needs urgent help. He has an hour and a half to prepare a report on the previous year's lottery results.
He received the data from his boss in a huge CSV file and a list of statistics that he must present to him.
You offered to help him. You will write a Python program that will analyze the data from this file and extract
all the necessary statistics for your friend. Implement the functions as described,
pay attention to the parameters (param), what to return (returns) and the return type (rtype). 
Implement as many functions as you can.
In order to pass the exam you should have at least 60% of tests passed.
'''


def get_draws(filename='lotto-result.csv'):
    """
    In CSV file you can find information about winnings on lottery from previous year.
    It contains: 6 lucky numbers separated with "-", name of month, day of draw, name of winner,
    prize, and city where winning took place.
    Implement function which will parse each file row into list and returns list of lists with all data from file

    :param filename: name of the file to be read
    :returns: list of lists representing draws data
    :rtype: list
    """
    results = []
    with open(filename, 'r') as file:
      rows = file.readlines()
    for row in rows:
      splitted_row = row.strip().split(",")
      result = []
      for row in splitted_row:
         result.append(row)
      results.append(result)
    return results
  
#get_draws()

def get_draw_numbers(numbers):
    """
    Implement a function which takes as an argument a string with numbers separated by hyphen (i.e. "9-7-2-13-4-12"),
    and puts all the numbers into a list of ints.

    :param numbers: string with hyphen("-") separated numbers
    :return: list of numbers
    :rtype: list of ints
    """
    str_list = numbers.split("-")
    int_list = []
    for i in str_list:
      i = int(i)
      int_list.append(i)
    return int_list

#get_draw_numbers("9-7-2-13-4-12")

def count_draws(draws):
    """
    Implement function that will count how many lottery wins were in last year.
    :param draws: list of lists with all draws
    :return: number of draws
    """    
    return len(draws)
#count_draws(get_draws())


def get_all_unique_drawn_numbers(draws):
    """
    Implement a function which will found all distinct numbers that were drawn in last year draws

    :param draws: list of lists with all draws
    :return: set of unique numbers
    """
    res = [item[0] for item in draws]
    new_list = []
    for i in res:
      numbers = get_draw_numbers(i)
      new_list.append(numbers)
    uniq = set(k for l in new_list for k in l)
    return uniq

#get_all_unique_drawn_numbers(get_draws())


def get_all_never_winning_numbers(draws):
    """
    Implement a function that will found numbers which never were drawn in last year

    :param draws: list of lists with all draws
    :return: set of unique numbers never drawn
    """
    res = [item[0] for item in draws]
    new_list =[]
    for i in res:
      numbers = get_draw_numbers(i)
      new_list.append(numbers)

    uniq = set(k for l in new_list for k in l)
    all_possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    set_numbers = set(all_possible_numbers)
    print((set(uniq) | set(set_numbers)) - (set(uniq) & set(set_numbers)))
    return (set(uniq) | set(set_numbers)) - (set(uniq) & set(set_numbers))

#get_all_never_winning_numbers(get_draws())


def get_dictionary_with_occurrences_of_drawn_numbers(draws):
    """
    Implement a function that will return a dictionary where the key will be a number that ever took part in draw,
    and the value will be a number of occurrences of that number in last year draws.
    :param draws: list of lists with all draws
    :return: dictionary
    """
    print(draws)
    res = [item[0] for item in draws]
    new_list =[]
    flat_list = []
    for i in res:
      numbers = get_draw_numbers(i)
      new_list.append(numbers)
    for element in new_list:
      if type(element) is list:
       for item in element:
             flat_list.append(item)
      else:
        flat_list.append(element)
    draw_dict = {}

    for j in flat_list:
      if j in draw_dict:
        draw_dict[j] +=1
      else:
        draw_dict[j] =1
    print(draw_dict)
    return draw_dict
    

#get_dictionary_with_occurrences_of_drawn_numbers(get_draws())


def get_most_winning_number(draws):
    """
    Implement a function that will return a number which took part in most winnings
    :param draws: list of lists with all draws
    :return: number
    :rtype: int
    """
    res = [item[0] for item in draws]
    new_list =[]
    flat_list = []
    for i in res:
      numbers = get_draw_numbers(i)
      new_list.append(numbers)
    for element in new_list:
      if type(element) is list:
        for item in element:
          flat_list.append(item)
      else:
        flat_list.append(element)
    draw_dict = {}

    for j in flat_list:
      if j in draw_dict:
        draw_dict[j] +=1
      else:
        draw_dict[j] =1
    max_value = max(draw_dict.values()) 
    max_keys = [k for k, v in draw_dict.items() if v == max_value]
    return(max_keys[0])
   
#get_most_winning_number(get_draws())

def get_list_of_numbers(draws):
    res = [item[0] for item in draws]
    new_list = []
    for i in res:
      numbers = get_draw_numbers(i)
      new_list.append(numbers)
    return new_list

def flat(draws):
    flatList = []
    for element in draws:
        if type(element) is list:
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList

def get_all_numbers(draws):
    """
    Implement a function that will return a list of all numbers drawn in every draw (with duplicates)
    :param draws: list of lists with all draws
    :return: sorted list of all drawn numbers
    """
    flat_list = sorted(flat(draws))
    print(flat_list)
    
get_all_numbers(get_list_of_numbers(get_draws()))

#nieprzeczytane

def get_highest_prize(draws):
    """
    Implement a function that finds the highest prize won in last year
    :param draws: list of lists with all draws
    :return: highest prize
    :rtype: float
    """
    new_list = []
    for col in draws:
        prizes = float(col[4])
        new_list.append(prizes)
    sorted_list = sorted(new_list)
    return sorted_list[-1]
get_highest_prize(get_draws())

def get_average_prize(draws):
    """
    Implement a function that counts the average winning in last year, rounded to two decimal places
    :param draws: list of lists with all draws
    :return: average winning
    :rtype: float
    """
    new_list = []
    sum_prizes = 0
    for col in draws:
        prizes = float(col[4])
        sum_prizes += prizes
        new_list.append(prizes)
    print(round(sum_prizes/len(new_list), 2))
    return round(sum_prizes/len(new_list), 2)
    
get_average_prize(get_draws())


def bubble_sort(arr):
    """
    Implement a function that will sort a list of strings in alphabetical order using bubble sort algorithm.
    :param arr: list of strings with names
    :return: sorted list
    """
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def get_sorted_list_of_unique_winners_names(draws):
    """
    Implement a function that will return a list of winners names, sorted in alphabetical order,
    do not use build-in methods, implement your own sorting algorithm
    :param draws: list of lists with all draws
    :return: list of strings alphabetically sorted
    """
    new_list = []
    for col in draws:
      winners = col[3]
      new_list.append(winners)
    print(bubble_sort(new_list))
get_sorted_list_of_unique_winners_names(get_draws())

def check_if_number_ever_been_drawn(draws, number):
  """
  Implement a function that will return True of False, depending on whether the given number ever been drawn.
  If the given number is out of range 1-49 inclusive, then method should raise ValueError.
  :param draws: list of lists with all draws
  :param number: checked number
  :raises ValueError: if the given number is out of range 1-49.
          Error message: "This number does not take part in the draw"
  :return: True or False
  """
  if number not in range(1, 50):
    raise ValueError("This number does not take part in the draw")
  for i in draws:
    for j in i:
      if number == j:
        return True
  
  return False

#print(check_if_number_ever_been_drawn(get_list_of_numbers(get_draws()), 49))


def generate_random_numbers():
    """
    Generate your own 6 numbers for lottery! Try your luck!
    Implement a method that returns list with 6 random, not repeating, positive integers between 1 and 49

    :return: list with 6 positive integers between 1 - 49 inclusive
    """
    num_list = []
    for i in range(6):
      random_num = random.randint(1, 49)
      num_list.append(random_num)
    return num_list
#generate_random_numbers()

def get_list_of_draws_in_month(draws, month):
    """
    Implement a function that will return a list of draws in particular month, if there was no winnings in specific
    month, function should return empty list. If name of month does not exists exception should be raised
    :param draws: list of lists with all draws
    :param month: name of month
    :raises ValueError: if the given month name is not a real month name.
            Error message: "Such month does not exists"
    :return: list of lists with draws for particular month
    """
    result = []
    if month.lower() not in ALL_MONTHS:
      raise ValueError("Such month does not exists")
    for i in draws:
      if i[1].lower() == month.lower():
        result.append(get_draw_numbers(i[0]))
    return result
get_list_of_draws_in_month(get_draws(), "October")


def get_month_with_most_number_of_winnings(draws):
    """
    Implement a function that will return a name of the month with the most winnings last year.
    :param draws: list of lists with all draws
    :return: lowercase name of month
    """
    months = []
    months_dict = {}
    for i in draws:
      months.append(i[1])
    for month in months:
      if month in months_dict:
        months_dict[month] += 1
      else:
        months_dict[month] = 1
    max_month = max(months_dict, key=months_dict.get)
    return max_month.lower()
#get_month_with_most_number_of_winnings(get_draws())  


def get_dict_with_cities_and_number_of_wins_in_them(draws):
    """
    Implement a function that will return a dictionary where the key would be a city name and value would be an integer
    with number of wins in that city in previous year
    :param draws: list of lists with all draws
    :return: dict
    """
    cities = []
    cities_dict = {}
    for i in draws:
      cities.append(i[5])
    for city in cities:
      if city in cities_dict:
        cities_dict[city] += 1
      else:
        cities_dict[city] = 1
    return cities_dict

get_dict_with_cities_and_number_of_wins_in_them(get_draws())

def get_list_with_top_5_winnings_in_last_year_descending(draws):
    """
    Implement a function that will return list with top 5 winnings in last year draws, starting from the biggest one
    :param draws: list of lists with all draws
    :return: list with top 5 winnings
    """
    wins = []
    for i in draws:
      wins.append(float(i[4]))
    result = sorted(wins, key = lambda x:float(x))[::-1]
    return result[::6]
    
get_list_with_top_5_winnings_in_last_year_descending(get_draws())