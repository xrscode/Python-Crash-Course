# def QuestionsMarks(str): 
#   a = 0 #Number Counter
#   b = 0
#   for i in str:
#     if i.isdigit():
#       if int(i) + a == 10:
#         b += 1
#       else: a = int(i)
#   return b
# print(QuestionsMarks("acc?7??sss?3rr1??????5"))
# print(QuestionsMarks("aa6?9"))
# print(QuestionsMarks("5a5a5a5"))

# def take(arr, n):
#   print(arr[:n])

# take([0, 1, 2, 3, 5, 8, 13], 3)

# def count_positives_sum_negatives(arr):
#     positive = 0
#     negative = 0
#     if not arr:
#         return []

#     for i in arr:
#         if i > 0:
#             positive += 1
#             print(i)
#         else:
#             negative += i
#     return [positive, negative]

# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

# Sum of a sequence: https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python
# def sequence_sum(begin_number, end_number, step):
#     num = 0
#     if begin_number > end_number:
#         return 0
#     else:
#         x = range(begin_number, end_number + 1, step)
#         for n in x:
#             num += n
#     return num

# Anagram Challenge: https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python
# def is_anagram(test, original):
#     if sorted(test.lower()) == sorted(original.lower()):
#         return True
#     else:
#         return False

# print(is_anagram("eeffot", "toffee"))

# Sum of Array: https://www.codewars.com/kata/53dc54212259ed3d4f00071c/solutions/python
# def sum_array(a):
#     if not a:
#         return 0
#     else:
#         num = 0
#         for i in a:
#             num += i
#         return num

# Two to one: https://www.codewars.com/kata/5656b6906de340bd1b0000ac/python
