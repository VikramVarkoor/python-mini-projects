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

images = [rock,paper,scissors]

user_choice = int(input("Choose 0 for rock, 1 for paper or 2 for scissors. \n"))
print(images[user_choice])
comp_choice = random.randint(0,2)
print("computer chose: ")
print(images[comp_choice])

if user_choice==0 and comp_choice==2:
    print("You win")
elif user_choice==2 and comp_choice==0:
    print("Computer wins")
elif comp_choice > user_choice:
    print("You lose")
elif comp_choice < user_choice:
    print("You win")
elif comp_choice==user_choice:
    print("Draw")
elif user_choice>=3 or user_choice<0:
    print("invalid number")



