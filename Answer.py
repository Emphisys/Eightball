from random import randrange


def numbergen():
  answer = ""
  random_number = randrange(12)
  if random_number == 1:
    answer = "Yes - definitely."
    return(answer)
  elif random_number == 2:
    answer = "It is decidedly so."
    return(answer)
  elif random_number == 3:
    answer = "Without a doubt."
    return(answer)
  elif random_number == 4:
    answer = "Reply hazy, try again."
    return(answer)
  elif random_number == 5:
    answer = "Ask again later."
    return(answer)
  elif random_number == 6:
    answer = "Better not tell you now."
    return(answer)
  elif random_number == 7:
    answer = "My sources say no."
    return(answer)
  elif random_number == 8:
    answer = "Outlook not so good."
    return(answer)
  elif random_number == 9:
    answer = "Very doubtful"
    return(answer)
  elif random_number == 10:
    answer = "In your wildest dreams!"
    return(answer)
  elif random_number == 11:
    answer = "Of course bloody -of course!-"
    return(answer)
  elif random_number == 12:
    answer = "YAAAS"
    return(answer)
  else:
    print("ERROR")




