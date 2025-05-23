print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Choose the direction: right or left? ").lower()

if choice1 == "left":
    choice2 = input("Arrived at a lake: swim or wait for the boat? ").lower()

    if choice2 == "wait":
        choice3 = input(
            "You arrived at a house with 3 doors: red, yellow, or blue. Which one will you choose? ").lower()

        if choice3 == "yellow":
            print("You win!! 🎉")
        elif choice3 == "blue":
            print("Entered a room of beasts. You die. 💀")
        elif choice3 == "red":
            print("Entered a room of fire. You die. 🔥")
        else:
            print("You chose a door that doesn't exist. You die. ❌")

    else:
        print("You drowned. GG. 🌊")

else:
    print("You fell into a trap. Game over. ❌")

