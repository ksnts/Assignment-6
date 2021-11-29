from random import randrange

num1 = randrange (0,99)
num2 = randrange (0,99)
score = 0
numItems = 1
qnum = 1

while numItems <=10:
    print(f"Question {qnum}: {num1} + {num2} =")
    userInput = input("Answer: ")
    qsum = num1 + num2

    if userInput == qsum:
        score+=1
    else:
        score-=1
    
    qnum +=1
    numItems +=1

print("Your score is: ", score)




