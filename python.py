# from Mary Shelley's Frankenstein
print("There is something at work in my soul, which I do not understand.")

print("Hello world!")

message_string = "Hello there"
# Prints "Hello there"
print(message_string)

# Greeting
message_string = "Hello there"
print(message_string)
 
# Farewell
message_string = "Hasta la vista"
print(message_string)

print('This message has mismatched quote marks!')
print('Abracadabra')

an_int = 2
a_float = 2.1
 
print(an_int + 3)
# Output: 5

# Prints "500"
print(573 - 74 + 1)
 
# Prints "50"
print(25 * 2)
 
# Prints "2.0"
print(10 / 5)

coffee_price = 1.50
number_of_coffees = 4
 
# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)
 
# Updating the price 
coffee_price = 2.00
 
# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# 2 to the 10th power, or 1024
print(2 ** 10)
 
# 8 squared, or 64
print(8 ** 2)
 
# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)
 
# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)


greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
 
# Prints "Hey there!How are you doing?"
print(full_text)
full_text = greeting_text + " " + question_text
 
# Prints "Hey there! How are you doing?"
print(full_text)

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
 
# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2
 
# Prints "I am 10 years old today!"
print(full_birthday_string)
 
# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.
 
# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)

# First we have a variable with a number saved
number_of_miles_hiked = 12
 
# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2
 
# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14

hike_caption = "What an amazing time to walk through nature!"
 
# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"

print(hike_caption)

leaves_of_grass = """
And here is an example of a multi-line string.  A string that takes up multiple lines.  What if we wanted to provide a quotation within our string? My dog dylan says; 'Woof, woof, woof!'.  The tripple quotation marks prevent us from closing the string too early!
"""

print(leaves_of_grass)

my_age = 35
half_my_age = 35/2
greeting = "Hi!  Nice to meet you."
name = "Simon"
greeting_with_name = greeting + " " + "My name is " + name + " and I am " + str(my_age) + "."
print(greeting_with_name)

#Prints: Hi!  Nice to meet you. My name is Simon and I am 35.
