"""
Name(s): Judith Weintraub
Name of Project: Hangman
"""
#Write the main part of your program here. Use of the other pages is optional.

import random
from PyDictionary import PyDictionary
import time
from page1 import state_names

correct_state = random.choice(state_names)
counter = 10
guesses = []
still_going = False
missed_letters = []
total_guesses = 0
#the instructions
print("Your word is", len(correct_state), "letters long."); time.sleep(1)
print("Guess all letters in lowercase.") ; time.sleep(1)
print("You can guess 10 wrong letters."); time.sleep(1)
print("And...go!")

while still_going == False:
  wronglettercount = 0
  #the main loop, checks if the guess is in the word
  for letter in correct_state: 
      if letter in guesses:
          print(letter, end=" ")
      else:
          print("_", end = " ")
          wronglettercount += 1
  if wronglettercount == 0:
    break
  print("")
  guess = input("Enter a letter: ")
  #checks if inputs are letters
  if str.isalpha(guess) == False:
    print("That's not a letter.")
  #checks if more than one letter is entered
  elif len(guess) > 1:
    print("Too many letters.")
  elif guess not in correct_state:
    missed_letters.append(guess)
    counter -= 1
    total_guesses += 1
  else:
    guesses.append(guess)
    total_guesses += 1

  print(" ")
  print("you have", counter, "wrong guesses left.")
  
  for letter in correct_state:
    if letter not in guesses:
      done = False
  #checks if done
  if counter == 0:
    break
  
if counter == 0:
  print("The word was", correct_state)
elif still_going == False:
  print("")
  print("You guessed the word in", total_guesses, "tries! It was", correct_state)

print(" ")
get_def = input("Enter yes to find out the definition of your word or no to end the game: ") 
#gets the definition
if get_def == "yes" or get_def == "Yes":
  dict = PyDictionary()
  meaning = dict.meaning(correct_state)
  print("")
  print(meaning); time.sleep(3)
elif get_def == "no":
  print("Goodbye.")
else:
  print("that's not a valid input.")
  print("I'm going to show you the definition anway.")
  dict = PyDictionary()
  meaning = dict.meaning(correct_state)
  print("")
  print(meaning); time.sleep(3)