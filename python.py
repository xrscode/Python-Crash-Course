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

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []
 
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
 
print(only_negative_doubled) 

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)

numbers = [2, -1, 79, 33, -45]
 
no_if   = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [num for num in heights if num > 161]


# Your code below:
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

for i in single_digits:
  print(i)
  squares.append(i**2)

print(squares)

cubes = [i**3 for i in single_digits]

print(cubes)