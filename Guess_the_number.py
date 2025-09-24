import random

number= random.randint(1, 25)
player_name = input("Hello What's your name?  " )
number_guess= 0
print("Alright", player_name , "I am guessing a number between 1 to 25" )

while number_guess < 5:
    guess=int(input())
    number_guess += 1
    if guess < number :
        print("Your are guessing  a lower number")
    if guess > number:
        print("You are guessing a higher value")
    if guess == number:
        break
if guess == number:
    print("You guessed the number in " + str(number_guess) + " tries")
else:
    print("You did not find the number, the number was" + str(number) + "!" )