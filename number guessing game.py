import random 
print("Number guessing game") 
number = random.randint(1, 9) 
chances = 0
print("Guess a number (between 1 and 9):")  
while chances < 5: 
    guess = int(input()) 
    if guess == number: 
        print(" YOU WON!!!") 
        break
    elif guess < number: 
        print("Your guess was low: Guess a higher number", guess) 
    else: 
        print("Your guess was high: Guess a lower number", guess) 
    chances += 1
if not chances < 5: 
    print("YOU LOSE!!! The guessed number is", number) 
