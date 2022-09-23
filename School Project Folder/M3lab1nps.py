import math
import random
import sys

name = input("What is your name")
print( str(name) )

answer = input('Do you want to continue?:')
if answer.lower().startswith("yes"):
      print("ok, carry on then")
elif answer.lower().startswith("no"):
      print("ok, byebye")
      exit()

def numberGuess():
  your_guess = random.randrange(1,11)
  guess = int(input("Try to guess the number:"))
  print (your_guess)
  while True:
    if (guess == your_guess):
        print ("You got it!")
        break
    if (guess > your_guess):
        print ("Wrong! You guessed too high")
        guess = int(input("Try to guess the number:"))
    if (guess < your_guess):
        print ("Wrong! You guessed too low")
        guess = int(input("Try to guess the number:"))

numberGuess()