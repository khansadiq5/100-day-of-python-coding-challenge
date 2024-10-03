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
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissore = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissore]
user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissore\n"))
if user >= 3 or user < 0:
    print("You type a invalid number,You Lose!") 
else:     
    print(game_images[user])
    computer = random.randint(0, 2)

    print("Computer choose:")
    print(game_images[computer])
 
    if computer == 2 and user == 0:
        print("You Win!")   
    elif computer == 0 and user == 2:
        print("You Lose!")           
    elif computer > user:
        print("You Lose!") 
    elif user > computer: 
        print("You Win!")           
    elif computer == user:
        print("Draw!")

  