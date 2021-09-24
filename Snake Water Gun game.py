# Snake water Gun game
import random
draw = 0
chance = 0
comp = 0
you = 0
i = 0
while (i < 10):
    user = input("enter s for snake, w for water, g for gun  ")
    list1 = ["snake", "water", "gun"]
    computer = random.choice(list1)
    if computer == "snake" and user == "w":
        print("Computer = snake \n You = water \n Computer won")
        comp = comp + 1
        chance = chance - 1
    elif computer == "snake" and user == "g":
        print("Computer = snake \n You = gun \n You won")
        you = you + 1
        chance = chance - 1
    elif computer == "water" and user == "s":
        print("Computer = water \n You = snake \n You won")
        you = you + 1
        chance = chance - 1
    elif computer == "water" and user == "g":
        print("Computer = water \n You = gun \n Computer won")
        comp = comp + 1
        chance = chance - 1
    elif computer == "gun" and user == "s":
        print("Computer = gun \n You = snake \n Computer won")
        comp = comp + 1
        chance = chance - 1
    elif computer == "gun" and user == "w":
        print("Computer = gun \n You = water \n You won")
        you = you + 1
        chance = chance - 1
    else:
        print("TIE")
        draw = draw + 1
        chance = chance - 1
    i = i + 1
print("Final Score: \n Computer= ", comp, "You= ", you, "Draws= ", draw)




