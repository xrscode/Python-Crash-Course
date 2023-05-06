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