#game development
#coding snake-water-gun game in python
#14th day of python(23 dec 2020)
print("welcome to the snake-water-gun game\n")
print("total number of chances: 10\n")
import random
computer_score = 0
user_score = 0
user_chance= 0
computer_choice = ["s","w","g"]
while(user_chance < 10 and user_score < 10 and computer_score < 10):
    print("enter s for snake, w for water or g for gun\n")
    user = input()
    computer =str(random.choice(computer_choice))
    print(computer)
    if user == "s" and computer == "w":
        print("you got a point, thirsty snake! you drank the water.")
        user_score = user_score + 1
        print("your score : ", user_score)
        print("computer score: ", computer_score)
    elif user == "w" and computer == "s":
        print("oops! you lost this chance. snake drank the water.")
        computer_score = computer_score + 1
        print("your score : ", user_score)
        print("computer score: ", computer_score)
    elif user == "g" and computer == "s":
        print("you got a point, killer! you killed the snake.")
        user_score = user_score + 1
        print("your score : ", user_score)
        print("computer score: ", computer_score)
    elif user == "s" and computer == "g":
        print("oops you lost this chance. killer killed the snake.")
        computer_score = computer_score + 1
        print("your score : ", user_score)
        print("computer score: ", computer_score)
    elif user == "w" and computer == "g":
        print("you got a point, dude! you drenched the gun")
        user_score = user_score + 1
        print("your score : ", user_score)
        print("computer score: ", computer_score)
    elif user == "g" and computer == "w":
        print("you lost this time, your gun has been drowned.")
        computer_score = computer_score + 1
        print("your score : ", user_score)
        print("computer score: ", computer_score)
    else:
        print("its a tie.")
        computer_score = computer_score + 1
        user_score = user_score + 1
        print("your score : ", user_score)
        print("computer score: ", computer_score)
    user_chance = user_chance + 1
    print("left chances: ",10-user_chance)
if user_score > computer_score:
    print("CONGRATULATIONS Dude! you won the game.")
elif user_score < computer_score:
    print("you lost the game. best of luck for the next time")
else:
    print("its a TIE.")









