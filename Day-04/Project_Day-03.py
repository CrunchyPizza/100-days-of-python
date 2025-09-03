rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random

game_images = [rock, paper, scissors]

flag = True
while flag:
    try:
        user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    except ValueError:
        print("Invalid input, please type a number (0, 1, or 2).")
        continue
    
    if user_input not in [0, 1, 2]:
        print("You typed an invalid number, you lose!")
    else:
        print("You chose:")
        print(game_images[user_input])  

        computer_input = random.randint(0, 2)
        print("Computer chose:") 
        print(game_images[computer_input])

        if user_input == computer_input:
            print("It's a draw")
        elif (user_input == 0 and computer_input == 2) or \
             (user_input == 1 and computer_input == 0) or \
             (user_input == 2 and computer_input == 1):
            print("You win!")
        else:
            print("You lose")

    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'n':
        flag = False
