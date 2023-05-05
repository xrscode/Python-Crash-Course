#User Input
likes_snakes = input("Do you like snakes? ")
print(likes_snakes)

>>> favorite_fruit = input("What is your favorite fruit? ")
What is your favorite fruit? mango
 
>>> print("Oh cool! I like " + favorite_fruit + " too, but I think my favorite fruit is apple.")
Oh cool! I like mango too, but I think my favorite fruit is apple.

1 == 1     # True
2 != 4     # True
3 == 5     # False
'7' == 7   # False

set_to_true = True
set_to_false = False

bool_one = 5 != 7 #True
bool_two = 1 + 1 != 2 #False
bool_three = 3 * 3 == 9 #True

print(bool_one)    # True
 
print(bool_two)    # False
 
print(bool_three)  # True

my_baby_bool = "true"
print(type(my_baby_bool))
#Prints: <class 'str'>

my_baby_bool_two = True
print(type(my_baby_bool_two))
#Prints: <class 'bool'>

if 2 == 4 - 2: 
  print("apple")

  # Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")

(1 + 1 == 2) and (2 + 2 == 4)   # True
(1 > 9) and (5 != 6)            # False
(1 + 1 == 2) and (2 < 1)        # False
(0 == 10) and (1 + 1 == 1)      # False

True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

not 1 + 1 == 2  # False
not 7 < 0       # True

statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

if not(credits >= 120):
  print("You do not have enough credits to graduate.")

if not(gpa >= 2.0):
  print("Your GPA is not high enough to graduate.")

if not(credits >= 120) and not ( gpa >= 2.0):
    print("You do not meet either requirement to graduate!")

    if weekday:
  print("wake up at 6:30")
else:
  print("sleep in")

print("Thank you for the donation!")
 
if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")