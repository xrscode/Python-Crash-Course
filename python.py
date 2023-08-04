# 🚨 Don't change the code below 👇
#two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
#print(int(two_digit_number[0]) + int(two_digit_number[1]))
#print(int('2') + int('3'))

# 🚨 Don't change the code below 👇
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(round(int(weight) / float(height)**2, 2))
#score = 5 #int
#height = 1.2 #float
#isWinning = True #boolean
#f-String
#print(f'Your score is {score} and your height is {height}')

#age = '13'
#yearsLeft = 90 - int(age)
#print(yearsLeft)

#Tip Calculator
totalBill = input('What was the total bill?')
percentage = input('What percentage tip would you like to give?')
split = input('How many people to split the bill?')
pc = int(percentage)/100 + 1
tb = float(totalBill)
sp = int(split)
bill = round((tb/sp)*pc, 2)
print(f'Each person should pay: {bill}')