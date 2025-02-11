import random

number = random.randint(1, 100)
attempts = 10

while attempts > 0 :
    guess = int(input("Guess the number: "))
    if guess > number :
        print("Too high! ")
        attempts = attempts-1
    elif guess == number :
        print("You guessed it right! ")
        break
    else :
        print("Too low! ")
        attempts = attempts-1

    if attempts == 0 :
        input1 = input(f"you lost. the number is {number}. want to play again? ")
        if input1 in ['Y', 'YES', 'y', 'yes', 'ok'] :
            attempts = 10
            number = random.randint(1, 100)

