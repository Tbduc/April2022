# def intToRoman(num):
#    result = ""
#    start_num = 0
#    val_list = [1, 5, 10, 50, 100, 500, 1000, 4, 9, 40, 90, 400, 900]
#    sorted_values = sorted(val_list, reverse=True)
#    key_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'IV', 'IX', 'XL', 'XC', 'CD', 'CM']
#    while num > 0:
#       for i in range(start_num, len(sorted_values)):
#          if num - sorted_values[i] >= 0:
#             num -= sorted_values[i]
#             result += key_list[val_list.index(sorted_values[i])]
#             start_num = i
#             break
#    return result

# print(intToRoman(27))


# def twoSum(nums, target):
#    for i in range(len(nums)):
#       for j in range(i+1, len(nums)):
#          result = nums[i] + nums[j]
#          if result == target:
#             return [i, j]

# print(twoSum([2,7,11,15], 9))

# def isPalindrome(x):
#    # number = str(x)
#    # if number == number[::-1]:
#    #    return True
#    # return False
#    rev = 0
#    temp = x
#    while(temp > 0):
#       rev = rev * 10 + (temp % 10)
#       temp = temp // 10
#    return rev == x

# print(isPalindrome(202))


from gc import get_referents


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
   with open(filename, 'r+') as file:
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
    print(len(draws))
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
   return (max(draw_dict, key=draw_dict.get))
   
get_most_winning_number(get_draws())