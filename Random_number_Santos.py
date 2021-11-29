#random num generator
from random import randrange
#variables for scoring
score = 0
numItems = 1
qnum = 1
#question loop
while numItems <=10:
    num1 = randrange (0,99)
    num2 = randrange (0,99)

    print("\n")
    print(f"Question {qnum}: {num1} + {num2} =")
    userInput = float(input("Answer: "))
    qsum = num1 + num2
    
#increments for the loop and scoring
    if userInput == qsum:
        score+=1
        print("Correct !")
    else:
        print("Wrong !")
    
    qnum +=1
    numItems +=1
#total score
print("\n")
print(f"Your total score is: {score}/10!")





