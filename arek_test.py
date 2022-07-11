import csv
import random

def get_draws(filename='lotto-result.csv'):    
    data_list = []
    with open(filename,'r')as file:
      file_content=csv.reader(file)
      for row in file_content:
        data_list.append(row)
    return data_list
def get_draw_numbers(numbers):
    return [int(i) for i in numbers.split('-')]
def count_draws(draws):
    return(len(draws)) 
def get_all_unique_drawn_numbers(draws):
    draw = []
    for i in draws:
        number_set = get_draw_numbers(i[0])
        for j in number_set:
            draw.append(j)
        draw_set =set(draw)
        return draw_set 
def get_all_never_winning_numbers(draws):
    never_draw = []
    draw = []
    for i in draws:
      number_set = get_draw_numbers(i[0])
      for j in number_set:
        draw.append(int(j))
    draw_set =set(draw)

    for i in draw_set:
        if i not in draw_set:
            never_draw.append(i)
    return set(never_draw) 
def get_dictionary_with_occurrences_of_drawn_numbers(draws):
    dictionery ={}
    draw = []
    for i in draws:
        number_set = get_draw_numbers(i[0])
        for j in number_set:
            draw.append(j)
    draw_set =set(draw)
    for i in draw_set:
        dictionery[i]=0
        for j in draw:
            if j == i:
                dictionery[i] +=1
    return dictionery
def get_most_winning_number(draws):
    dictionery ={}
    draw = []
    for i in draws:
        number_set = get_draw_numbers(i[0])
        for j in number_set:
            draw.append(j)
    draw_set =set(draw)

    for i in draw_set:
        dictionery[i]=0
        for j in draw:
            if j == i:
                dictionery[i] +=1
    max_key = max(dictionery.keys(), key=(lambda k: dictionery[k]))
    return max_key
def get_all_numbers(draws):
         return [get_draw_numbers(i[0]) for i in draws]
def get_highest_prize(draws):
    high_price = 0 
    for i, value in enumerate(draws):
        if float(value[4]) > high_price:
            high_price = float(value[4])
    return high_price
def get_average_prize(draws):
    value_pay = 0
    for i in draws:
        value_pay += float(i[4])
    average_pay = value_pay/len(draws)
    return round(average_pay,2)

def get_sorted_list_of_unique_winners_names(draws):
      return sorted(set([i[3] for i in draws]))
def bubble_sort(arr):
    arr = [i[3] for i in arr] #list created from names taken from draws list
    elements_in_list = len(arr)
    for i in range(elements_in_list):
        for j in range(elements_in_list - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def check_if_number_ever_been_drawn(draws, number):
    draw = []
    for i in draws:
        number_set = get_draw_numbers(i[0])
        for j in number_set:
            draw.append(j)
    draw_set =set(draw)
    if number not in range(49):
        print('This number does not take part in the draw')
        raise ValueError
    else:
        if int(number) in draw_set:
            return True
        else:
            return False
def generate_random_numbers():
    number_generated =[]
    for i in range(6):
        test = True
        while test == True:
            number = random.randint(1,49)
            if number in number_generated:
                test = True
            else:
                number_generated.append(number)
                test = False
    return number_generated