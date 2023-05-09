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
# calculate_taxi_price(100, 10, 5)

# def calculate_taxi_price(miles_to_travel, rate, discount = 10):
#   print(miles_to_travel * rate - discount )

# # Using the default value of 10 for discount.
# calculate_taxi_price(10, 0.5)
 
# # Overwriting the default value of 10 with 20
# calculate_taxi_price(10, 0.5, 20)
# Write your code below:
max_price = max(9.75, 15.50, 5.99, 2.00)
print(max_price)

min_price = min(9.75, 15.50, 5.99, 2.00)
print(min_price)


rounded_price = round(tshirt_price, 1)
print(rounded_price)

rounded_price = round(tshirt_price, 1)
print(rounded_price)

def trip_welcome(destination):
  print(" Looks like you're going to the " + destination + " today. ")

budget = 1000
 
# Here we are using a default value for our parameter of `destination` 
def trip_welcome(destination="California"):
    print(" Looks like you're going to " + destination)
    print(" Your budget for this trip is " + str(budget))
 
print(budget)
trip_welcome()

def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate
 
new_zealand_exchange = calculate_exchange_usd(100, 1.4)
 
print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")

weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']
 
def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day

monday, tuesday, wednesday = threeday_weather_report(weather_data)
 
print(monday)
print(tuesday)
print(wednesday)

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third 
  
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)