print("Let's take quiz on SDG-17 goals")
score=0
print("Q1. Full Form Of SDG is?")
print("a. Sustainable Devlopment Goals")
print("b. Sustainable Deployment Goals")
print("c. Sustainable Demonstrative Goals")
answer=input("enter your choice    ")
if answer == "a":
  print("correct answer")
  score=score+10
else:
  print("wrong answer")
  score=score-5
print("Q2 By what year should we reach our SDG's?")
print("a. 2050")
print("b. 2030")
print("c. 2055")
answer=input("enter your choice    ")
if (answer=="b"):
  print("correct answer")
  score=score+10
else:
  print("wrong answer")
  score=score-5
print("What SDG is number 4?")
print("a. Quality Education")
print("b. No Poverty")
print("c. Clean water and Sanitation")
answer=input("enter your choice    ")
if (answer=="a"):
  print("correct answer")
  score=score+10
else:
  print("wrong answer")
  score=score-5
print("Your Score is",score)
