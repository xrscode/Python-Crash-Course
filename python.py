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
def SimpleSymbols(strParam):
    if strParam[0].isalpha() or strParam[-1].isalpha():
        return 'false'  # First or last character is a letter, not surrounded by '+'

    for i in range(1, len(strParam) - 1):
        if strParam[i].isalpha():
            if strParam[i - 1] != '+' or strParam[i + 1] != '+':
                return 'false'  # Letter is not surrounded by '+'

    return 'true'  # All letters are surrounded by '+'

# Example usage:
input_str = "+d+=3=+s+"
result = SimpleSymbols(input_str)
print(result)  # Output: "true"

input_str = "f++d+"
result = SimpleSymbols(input_str)
print(result)  # Output: "false"

SimpleSymbols('+a+b++++c+')


