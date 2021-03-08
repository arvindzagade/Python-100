rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_images = [rock,paper,scissors]
user_choice = int(input('Type 0 for Rock, 1 for paper or 2 for scissors\n'))
if user_choice >=3 or user_choice<0:
  print('you typed an Invalid Number,You Lose!')
else:

  print(game_images[user_choice])

  computer_choice = random.randint(0,2)
  print("computer chose: ")
  print(game_images[computer_choice])


  if user_choice == 0 and computer_choice==2:
    print('You Win!')
  elif computer_choice ==0 and user_choice==2:
    print('Computer Wins')
  elif computer_choice > user_choice:
    print('You Lose!')
  elif user_choice > computer_choice:
    print('You Win!')
  elif computer_choice == user_choice:
    print("It's a Draw!")
