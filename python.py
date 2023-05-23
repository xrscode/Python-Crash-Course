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

# def SimpleAdding(num):
#   a = 0
#   while num >= 0:
#     a += num
#     num -= 1
#   print(a)
#   return a


#   # code goes here
#   return a

# SimpleAdding(4)
# keep this function call here 

#print(SimpleAdding(input()))



##  Capitalise First Letter
# def LetterCapitalize(strParam):
#   new_list_upper = []
#   for i in strParam.split():
#     new_list_upper.append(i[0].upper() + i[1:])
#   return ''.join(new_list_upper)

# # keep this function call here 
# print(LetterCapitalize("i love coding"))


# Symbols Challenge
# def SimpleSymbols(strParam):
#     if strParam[0].isalpha() or strParam[-1].isalpha():
#         return 'false'  # First or last character is a letter, not surrounded by '+'

#     for i in range(1, len(strParam) - 1):
#         if strParam[i].isalpha():
#             if strParam[i - 1] != '+' or strParam[i + 1] != '+':
#                 return 'false'  # Letter is not surrounded by '+'

#     return 'true'  # All letters are surrounded by '+'

# # Example usage:
# input_str = "+d+=3=+s+"
# result = SimpleSymbols(input_str)
# print(result)  # Output: "true"

# input_str = "f++d+"
# result = SimpleSymbols(input_str)
# print(result)  # Output: "false"

# SimpleSymbols('+a+b++++c+')

#Power of 2
# import math
# def pow_of_two(num):
#     base = math.log(num, 2)
#     new_num = math.pow(2, base)
#     if(base.is_integer()):
#         print(str(base) + " is an integer of " + str(num))
#         print("Because 2, to the power of " + str(base) + " is equal to " + str(num))
#     else:
#         print(str(num) + " is not an integer of " + str(num))
#         print("Because the exponent of 2 would have to be: " + str(base))
# pow_of_two(124)

# def ArithGeo(arr):
#     is_arithmetic = False
#     is_geometric = False
#     is_neither = False
#     for i in range(len(arr) - 2):
#         if(arr[i + 1] - arr[i]) == (arr[i+2] - arr[i+1]) in range(arr[0], arr[len(arr)-2], 1):
#             is_arithmetic = True
#         elif(arr[i+1] / arr[i]) == (arr[i+2] / arr[i+1]) in range(arr[0], arr[len(arr)-2], 1):
#             is_geometric = True
#         else:
#             is_neither = True

#     if(is_arithmetic == True):
#       return 'Arithmetic'
#     elif(is_geometric == True):
#       return 'Geometric'
#     elif(is_neither == True):
#       return '-1'

# print(ArithGeo([1,2,3,4,5,10,20]))
# ArithGeo([2, 4, 16, 24])

# def ArrayAdditionI(arr):
#   arr_sorted = sorted(arr)
#   lrgest = arr_sorted[-1]
#   return lrgest

# print(ArrayAdditionI([5, 7, 16, 1, 2]))

# def LongestWord(sen):
#   new_sentence = ''
#   longest_word = ''
#   for char in sen:
#     if (char.isalpha() or char.isspace() or char.isnumeric()):
#       new_sentence += char
#   cleaned_split = new_sentence.split()
#   print(cleaned_split)
#   for word in cleaned_split:
#    if(len(word) > len(longest_word)):
#      longest_word = word
#    elif(len(word) == len(longest_word)):
#       continue
#   return longest_word
    

# LongestWord("I love dogs")

  
def QuestionsMarks(strParam):
  for i in strParam:
    if 
    



  

# QuestionsMarks("aa6?9")
QuestionsMarks("acc?7??sss?3rr1??????5")