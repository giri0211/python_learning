import random

roll = random.randint(1,6)
print("cmputer rolled "+ str(roll))
guess = int(input("Guess the roll: \n"))
if guess == roll:
    print("Correct !  you guess right roll is "+ str(roll))
else:
    print("next time !3")