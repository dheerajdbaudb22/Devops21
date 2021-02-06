import random

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
game_image = [rock, paper, scissors]
user_choice = int(input('Please select follwing any one 0 for "Rock", 1 for "paper" and 2 for "scissors" \n'))

if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!") 
else:
    print(game_image[user_choice])
    computer_choice = random.randint(0, 2)
    print("computer choose:")
    print(game_image[computer_choice])    
if user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif user_choice == 2 and computer_choice == 1:
    print("you win")
elif computer_choice == 2 and user_choice == 1:
    print("you lose")
elif user_choice == 1 and computer_choice == 0:
    print("you win")
elif computer_choice == 1 and user_choice == 0:
    print("you lose")
elif user_choice == computer_choice:
    print("Its a draw")




