# def LetterChanges(strParam):
#   vowels = ['a', 'e', 'i', 'o', 'u']
#   new_string = ""
#   for i in strParam:
#     if i.isalpha():
#         if (chr(ord(i)+1)) in vowels:
#           new_string += (chr(ord(i)+1)).upper()
#         else:
#           new_string += (chr(ord(i)+1))
#     else:
#       new_string += i 
#   return new_string
  
# print(LetterChanges("Hi!  My name is Dylan."))

#First Factorial Challenge
# def FirstFactorial(num):
#   a = 1
#   while num > 0:
#     a = a * num
#     num -= 1
#   # code goes here
#   print(a)
#   return a

# # keep this function call here 
# FirstFactorial(8)

#Simple Addition

def SimpleAdding(num):
  a = 0
  while num >= 0:
    a += num
    num -= 1
  print(a)
  return a


  # code goes here
  return a

SimpleAdding(4)
# keep this function call here 

#print(SimpleAdding(input()))

