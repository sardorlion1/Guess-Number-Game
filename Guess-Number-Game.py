import random

Tries = 0
guess = 0

name = input(("Hello, Welcome to the 'Guess Number Game' \nTo start the game Enter your name here : "))
number = random.randint(1, 320)

print("Hi, " + name + "!, I am thinking of a number between 1 and 20\nYou have six tries to find my guess number")
while Tries < 6:
    try:
        guess = int(input("Take a guess: "))  
        Tries = Tries + 1

        if guess < number:
            if number - guess <=3:
                print("Your guess is a little bit lower.;)")    
            else :
                print("Your guess is too low.")
                
        if guess > number:  
            if guess - number <=3:
                print("Your guess is a little bit higher.;)")  
            else:
                print("Your guess is too high.")#+str(number)
        else:
            if guess == number:
                break      
    except TypeError and ValueError:
        print("Please enter valid number!:(")

if guess == number:
    Tries = str(Tries)
    print('Well Done, ' + name + '! You guessed my number in' + Tries + ' guesses! :-D')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)