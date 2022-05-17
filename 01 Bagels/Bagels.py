# This is the bagels, a deductive logic game.
import random

print ("I am thinking of a 3-digit number. Try to guess what it is.")
print ("Here are some clues:")
print ("When I say:    That means:")
print("Pico            One digit or some digits is/are correct but in the wrong position.")
print("Fermi           One digit or some digits is/are and in the right position.")
print("Bagels          No digit is correct.")
print("I have thought up a number.")
print("You have 10 guesses to get it.")

number = [random.randint (0,9),random.randint (0,9) ,random.randint (0,9)]

no1= ()
no2= ()
no3= ()
guess = [no1,no2,no3]


for i in range (9):
    no1= int(input())
    no2= int(input())
    no3= int(input())
    guess = [no1,no2,no3]
    print ("Guess # " + str(i+1) + str(guess))

    if (guess[0] == number[0]) and (guess[1] == number[1]) and (guess[2] == number[2]):
        print ("You got it!")
        break

    elif (guess[0] == number[0]) or (guess[1] == number[1]) or (guess[2] == number[2]):
        print ("Fermi")

    elif (guess[0] == number[1]) or (guess[0] == number[2]) or (guess[1] == number[0]) or (guess[1] == number[2]) or (guess[2] == number[0]) or (guess[2] == number[1]) :
        print ("Pico")

    else :
        print ("No digit is correct")
