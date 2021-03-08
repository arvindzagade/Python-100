from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#Function to check user's guess against actual answer.
def check_answer(guess,answer,turns):
  """Checks answer against guess. Returns no. of turns remaining"""
  if guess > answer:
    print("Too High")
    return turns -1
  elif guess < answer:
    print('Too Low')
    return turns -1
  else:
    print(f"You got it!, The answer was {answer}")
  
#Make function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty.Type 'easy' or 'hard': ")
  if level =="easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  print(logo)
  #Choosing a random number between 1 to 100.

  print("Welcome to the guessing game!")
  print("I'm thinking about number between 1 and 100.")
  answer = randint(1,100)
  print(f"Actual ans is {answer}")

  turns = set_difficulty()



  #Repeat the functionality if they get it wrong
  guess = 0
  while guess!= answer:
    print(f"You have {turns} attempts remaining to guess the numbers")
    #Let the user guess the number.
    guess = int(input("Make a guess: "))

  # Track the no. of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("You've ran out of guesses,You lose!")
      return
    elif guess!= answer:
      print("Guess Again!")


game()