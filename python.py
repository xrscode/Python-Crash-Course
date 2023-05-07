#Lists
heights = [61, 70, 67, 64]

ints_and_strings = [1, 2, 3, "four", "five"]
mixed_list_common = ["Mia", 27, False, 0.5]

empty_list = []

append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')
 
print(append_example)

garden = ["Tomatoes", "Grapes", "Cauliflower"]
 
# Append a new element
garden.append("Green Beans")
print(garden)

items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)

my_list + [4]

calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]

print(calls[2])

pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]

print(pancake_recipe[-1])

garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries"
 
print(garden)

["Tomatoes", "Green Beans", "Strawberries", "Grapes"]

garden[-1] = "Raspberries"
 
print(garden)

shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]

shopping_line.remove("Chris")
 
print(shopping_line)

# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
# Remove a element
shopping_line.remove("Chris")
print(shopping_line)

heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]

#A 2d list with three lists in each of the indices. 
tic_tac_toe = [
            ["X","O","X"], 
            ["O","X","O"], 
            ["O","O","X"]
]

heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]

#Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height)

#Your code below:
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)


# The list of Jenny is at index 0. The hobby is at index 1. 
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)

customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

customer_data[2][2] = False

customer_data[1].remove(False)

store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")
print(store_line) 

cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
removed_element = cs_topics.pop()
print(cs_topics)
print(removed_element)

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

my_list = range(2, 9)
print(list(my_list))

my_range2 = range(2, 9, 2)
print(list(my_range2))

my_range3 = range(1, 100, 10)
print(list(my_range3))

my_list = [1, 2, 3, 4, 5]
 
print(len(my_list))

letters = ["a", "b", "c", "d", "e", "f", "g"]

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]
print(beginning)

# Your code below: 
middle = suitcase[2:4]
print(middle)

fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
fruits[:n]

fruits[:-n]

fruits[4:]
fruits[:-1]

list[first:last]

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters.count("i")
print(num_i)

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
num_pairs = number_collection.count([100, 200])
print(num_pairs)

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()
print(names)

names.sort(reverse=True)
print(names)

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
sorted_names = sorted(names)
print(sorted_names)