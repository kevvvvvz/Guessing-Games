import sys
import random

lower = int(input("Enter the lower bound #: "))
upper = int(input("Enter the upper bound #: "))

systemnum = random.randint(lower, upper)

rangesize = upper - lower + 1
guessbound = 0
while 2**guessbound < rangesize:
    guessbound = guessbound + 1
    
#print(guessbound)
    
guessallowed = 0
while True:
    #print("Bound:", guessbound)
    try:
        guess = int(input("Enter a guess to find the random number: "))
        guessallowed = guessallowed + 1
        #print(guessallowed)
        if guess == systemnum:
            print("Congratulations! You guessed the number in", guessallowed, "tries.")
            sys.exit()
        elif guessallowed == guessbound:
            print("Better Luck Next Time! Correct Number:", systemnum)
            sys.exit()
        elif guess < systemnum:
            print("Try Again! You guessed too small.")
            #break
        elif guess > systemnum:
            print("Try Again! You guessed too high.")
            #break
    except ValueError:
        print("Please enter a valid number!")
        
    