def QuestionsMarks(str): 
  a = 0 #Number Counter
  b = 0
  for i in str:
    if i.isdigit():
      if int(i) + a == 10:
        b += 1
      else: a = int(i)
  return b
print(QuestionsMarks("acc?7??sss?3rr1??????5"))
print(QuestionsMarks("aa6?9"))
print(QuestionsMarks("5a5a5a5"))