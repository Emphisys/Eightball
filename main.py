from Name import *
from Q import enter_question
from Answer import numbergen



def program():
  print(enter_name(), "\n")
  print(enter_question(), "\n")
  print("Magic 8-Ball's Answer:", numbergen(), "\n")
  #print(enter_name, " asks: ", enter_question, "\n", "Magic 8-Ball's Answer: ", numbergen)

def restart():
  res =input("Would you like to try again? If so, press 'r'")
  print("\n")
  if res == "r":
    program()
    restart()
  elif res == "R":
    program()
    restart()
  else:
    res == "closes"


program()
restart()


