
from art import logo,vs
import random
from game_data import data
from replit import clear

#Format account data into printable format.
def format_data(account):
  """Takes the account data and returns printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return (f"{account_name}, a {account_descr} from {account_country}")


def check_answer(guess,a_followers,b_followers):
  """ Take the user guess and follower counts and return if they got it right.."""
  if a_followers > b_followers:
    return guess =="a" 
      
  else:
    return guess == "b"
      


#Display arts 
print(logo)
# Game Score
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable.

while game_should_continue:
    
  # Generate a random account from the data
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  #Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  #Check if user is correct.
  ## Get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  # use if statement to check  if user is correct.
  is_correct = check_answer(guess,a_follower_count,b_follower_count)

  # Clear the screen between the rounds()
  clear()
  print(logo)
  # Give user feedback on their guess.
  #Score keeping
  if is_correct:
    score += 1
    print(f"You are right! Current Score {score}")
  else:
    game_should_continue= False
    print(f"Sorry,that's wrong. Final score: {score}")





# making account at position B become the next account at position A.

# Clear the screen between the rounds.
