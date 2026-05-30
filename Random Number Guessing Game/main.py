import random

input("Guessing Game\nPress anything to view the rules..")
input("I generate a number and you try to guess whether its higher or lower")
attempts=0
number=random.randint(1, 100)
print("Number is between 1-100")
while True:
    guess=input("Guess: ")
    try:
        guess=int(guess)
    except:
        print("Error: That is not a valid number. I need a digit.")
        continue

    attempts+=1
    if guess < number:
        print("Higher!")
    elif guess > number:
        print("Lower!")
    else:
        print(f"Congrats! the correct answer is {number}")
        input(f"you got it in {attempts} attempts!")
        break


