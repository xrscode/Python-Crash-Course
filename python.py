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