# print("Setting the Empire State Building as the starting point and Times Square as our destination.")
 
# print("Calculating the total distance between our points.") 
 
# print("The best route is by train and will take approximately 10 minutes.") 

# def function_name():
#   # functions tasks go here

# def trip_welcome():
#     print("Welcome to Tripcademy!") 
#     print("Let's get you to your destination.")

# trip_welcome()

# def trip_welcome():
#   # Indented code is part of the function body
#   print("Welcome to Tripcademy!") 
#   print("Let's get you to your destination.")
 
# # Unindented code below is not part of the function body
# print("Woah, look at the weather outside! Don't walk, take the train!")
 
# trip_welcome()

# def trip_welcome():
#   print("Welcome to Tripcademy!") 
#   print("Looks like you're going to Times Square today.")
 
# trip_welcome()

# def trip_welcome(destination):
#   print("Welcome to Tripcademy!") 
#   print("Looks like you're going to " + destination + " today.")

#   def my_function(parameter1, parameter2, parameter3):
#     # Some code

def trip_welcome(origin, destination):
  print("Welcome to Tripcademy")
  print("Looks like you are traveling from " + origin)
  print("And you are heading to " + destination)

def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )

# 100 is miles_to_travel
# 10 is rate
# 5 is discount
calculate_taxi_price(100, 10, 5)

def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )

# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)
 
# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)