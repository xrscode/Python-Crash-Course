print(favorite_fruit[:4])
# Output: blue
 
print (favorite_fruit[4:])
# Output: berry

fruit_prefix = "blue"
fruit_suffix = "berries"
favorite_fruit = fruit_prefix + fruit_suffix
 
print(favorite_fruit)
# Output: blueberries

favorite_fruit = 'blueberry'
print(favorite_fruit[-1])
# => 'y'
 
print(favorite_fruit[-2])
# => 'r'
 
print(favorite_fruit[-3:])
# => 'rry'

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]

favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""

def print_each_letter(word):
  for letter in word:
    print(letter)

favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)

print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False

print("blue" in "blueberry")
# => True
print("blue" in "strawberry")
# => False

print("e" in "blueberry" and "e" in "carrot")
# => False
print("e" in "blueberry" and not "e" in "carrot")
# => True

def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password