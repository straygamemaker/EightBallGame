
#writing magic 8 ball answers to questions
import random
endEightball = "stop"

eightBall = ["Try again later... ", "Yes! " , "I do not think so ", "Trust your gut "]
#responses = random.choice(eightBall)
usersQuestion = 0

while usersQuestion != "stop":
    usersQuestion = input("Ask the 8 ball a question. Type stop if you are done. ")
    print(random.choice(eightBall))
    if usersQuestion == endEightball:
        print("You have finished asking questions. ")
        break