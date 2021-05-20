def enter_question():
    question = input("What is your Yes or No question? ")
    if question == "":
        return("Are you trying to break me?")
    else:
        return("Your question is: " + question)