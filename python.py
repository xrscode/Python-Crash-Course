# for <temporary variable> in <collection>:
#   <action>

# ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
 
# for ingredient in ingredients:
#   print(ingredient)

#   for i in ingredients:
#   print(i)
#   for item in ingredients:
#  print(item)

# for ingredient in ingredients:
#   # Any code at this level of indentation 
#   # will run on each iteration of the loop
#   print(ingredient)

#   for ingredient in ingredients: print(ingredient)

#   for <temporary variable> in <list of length 6>:
#   print("Learning Loops!")

#   six_steps = range(6)
 
# # six_steps is now a collection with 6 elements:
# # 0, 1, 2, 3, 4, 5

# for temp in range(6):
#   print("Learning Loops!")

#   for temp in range(6):
#   print("Loop is on iteration number " + str(temp + 1))


# promise = "I will finish the python loops module!"

# for temp in range(5):
#   print(promise)

#   while <conditional statement>:
#   <action>

# count = 0
# while count <= 3:
#   # Loop Body
#   print(count)
#   count += 1

#   count = 0
# while count <= 3: print(count); count += 1

# ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

# length = len(ingredients)
# index = 0
 
# while index < length:
#   print(ingredients[index])
#   index += 1

# items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie", "knit dress"]

# for item in items_on_sale:
#   if item == "knit dress":
#     print("Found it")

# items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
 
# print("Checking the sale list!")
 
# for item in items_on_sale:
#   print(item)
#   if item == "knit dress":
#     break
 
# print("End of search!")

# big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
# for i in big_number_list:
#   if i <= 0:
#     continue
#   print(i)
# project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

# for team in project_teams:
#   print(team)

#   for team in project_teams:
#   # Loop elements in each sublist
#   for student in team:
#     print(student)

# sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

# scoops_sold = 0

# for location in sales_data:
#   print(location)
#   for i in location:
#     scoops_sold += i

# print(scoops_sold)

# numbers = [2, -1, 79, 33, -45]
# doubled = []
 
# for number in numbers:
#   doubled.append(number * 2)
 
# print(doubled)

# numbers = [2, -1, 79, 33, -45]
# doubled = [num * 2 for num in numbers]
# print(doubled)

# numbers = [2, -1, 79, 33, -45]
# only_negative_doubled = []
 
# for num in numbers:
#   if num < 0: 
#     only_negative_doubled.append(num * 2)
 
# print(only_negative_doubled) 

# numbers = [2, -1, 79, 33, -45]
# negative_doubled = [num * 2 for num in numbers if num < 0]
# print(negative_doubled)

# numbers = [2, -1, 79, 33, -45]
# doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
# print(doubled)

# numbers = [2, -1, 79, 33, -45]
 
# no_if   = [num * 2 for num in numbers]
# if_only = [num * 2 for num in numbers if num < 0]
# if_else = [num * 2 if num < 0 else num * 3 for num in numbers]

# heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

# can_ride_coaster = [num for num in heights if num > 161]


# # Your code below:
# single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# squares = []

# for i in single_digits:
#   print(i)
#   squares.append(i**2)

# print(squares)

# cubes = [i**3 for i in single_digits]

# print(cubes)

# words = ['quite', 'nice', 'really']
# for word in words:
#     for letter in word:
#         if not letter in 'aeiou':
#           print(letter, end='*')
#     print()


# for i in range(3):
#   print(5, end=' ')

# for i in range(45):
#   if i >=13:    
#     break
#   print(i, end='')

#   words = ['let', 'us', 'eat', 'some', 'rye', 'bread']
# ywords = []
 
# for word in words:
#   if 'y' in word:
#     ywords.append(word)
    
# print(ywords)

# groups = [["Alice", "Bob"], ["Carl", "David", "Elise"], ["Francis", "Georgia"]]
 
# i = 1
# for group in groups:
#   print("Group " + str(i) + " members:",)
#   i = i + 1
 
#   for name in group:
#     print(name, end=' ')

# names = ["Zara", "Saba", "Gigi", "Brea", "Abby", "Loki"]
# short_list = [name for name in names if name[3] == "a"]
# print(short_list)

# for name in names:
#   if name[3] == "a":
#     print(name, end=' ')

# [i-1 for i in range(5)]

# numbers = [1, 1, 2, 3]
# for number in numbers:
#   if number % 2 == 0:
#     continue
#   print(number)

# list_of_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# list_of_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(list_of_numbers[2])
# index = 0
# while 5 > index:
#   print(list_of_numbers[index])
#   index = index + 1


# list_of_accessories = ["Signpost", "Sculpture", "Gauge", "Feeder"]
# for item in list_of_accessories:
#   if item == "Gauge":
#     continue
#   print(item)

# exams = ["Physics", "History", "Linear Algebra"]
# for exam in exams:
#   if exam == "History":
#     break
#   print(exam)
# print("I finished!")

# prices = [15.0, 10.0, 7.5, 50.0]
# new_prices = [price * 0.8 for price in prices]
# print(new_prices)

# import random 
# credit = 25
# while credit > 0:
#   print('credit remaining:', credit)
#   amount = random.randint(1, 6)
#   spend = min(amount, credit)
#   print('credit spent:', spend)
#   credit -= spend
# print('credit remaining:', credit)

# import random 
# credit = 25
# while credit > 0:
#   print('credit remaining:', credit)
#   amount = random.randint(1, 6)
#   spend = min(amount, credit)
#   print('credit spent:', spend)
#   credit -= spend
# print('credit remaining:', credit)

# my_list = [5, 10, -2, 8, 20]
# desired_list = [10, 8, 20]

# [i for i in my_list i > 5]

# for i in range(3):
#   print(i)

# for i in range(3):
#   print(5)

# hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
# new_prices = [25, 20, 35, 15, 15, 30, 45, 30]

# cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

# print(cuts_under_30)

# print(range(len(hairstyles)))

# def divisible_by_ten(nums):
#   yes = 0
#   for i in nums:
#     if i % 10 == 0:
#       yes += 1
#   return yes

# def add_greetings(names):
#     list = []
#     list.append("Hello, " + names)
#     return list

# def add_greetings(names):
#     list = []
#     for i in names:
#       list.append("Hello, " + str(i))
#     return list

# def delete_starting_evens(my_list):
#   while (len(my_list) > 0 and my_list[0] % 2 == 0):
#     my_list = my_list[1:]
#   return my_list

# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))

# print(8 % 2 == 0)

# def dog(my_list):
#     return my_list[3:9]

# print(dog([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,]))

# def odd_indices(my_list):
#     newlist = []
#     for i in range(1, len(my_list), 2):
#         newlist.append(my_list[i])
#     return newlist

# def exponents(bases, powers):
#   new_list = []
#   for base in bases:
#     for power in powers:
#       new_list.append(base ** power)
#   return new_list
# print(exponents([2, 3, 4], [1, 2, 3]))

# def larger_sum(lst1, lst2):
#     sum1 = 0
#     sum2 = 0
#     for i in lst1:
#         sum1 += i
#     for i in lst2:
#         sum2 += i
#     if sum1 >= sum2:
#         return lst1
#     else:
#         return lst2

# def over_nine_thousand(lst):
#   sum = 0
#   for number in lst:
#     sum += number
#     if (sum > 9000):
#       break
#   return sum
# print(over_nine_thousand([8000, 900, 120, 5000]))
# print(over_nine_thousand([8000, 900]))

# def max_num(nums):
#     lrg = nums[0]
#     for number in nums:
#         if number > lrg:
#             lrg = number
#     return lrg
# print(max_num([50, -10, 0, 75, 20]))

