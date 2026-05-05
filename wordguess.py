import sys
import random

name = input("What is your name? ")
print("Good Luck!", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

print("Guess the characters")

turns = 12
guesses = ''
while turns > 0:
    failed = 0
    
    for char in word:
        if char in guesses:
            print(char,  end=" ")
        else:
            print("_", end=" ")
            failed += 1
        
    print()
    if failed == 0:
        print("You Win")
        print("The word is:", word)
        break
    
    #print()
    guess = input("Enter a character guess: ").lower().strip()
    if len(guess) != 1:
        print("Please enter only ONE character.")
        continue
    
    if guess in guesses:
            print("You already guessed that letter.")
            continue
        
    if guess not in guesses:
        guesses += guess
        
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, "more guesses")
        
    if turns == 0:
        print("You lose. The word was:", word)
        break
    
        
        

        