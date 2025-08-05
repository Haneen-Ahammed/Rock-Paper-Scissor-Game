import random

options=("rock","paper","scissors")

computer=random.choice(options)
point=0
com=0
while True:
    player=input("Enter the choice: ")
    if computer==player:
        print("No points")
    elif player=="rock":
        if computer=="paper":
            com+=1
            print(f"Player={point} and Computer {com}")
        else:
            point+=1
            print(f"Player={point} and Computer {com}")
    elif player=="paper":
        if computer=="scissors":
            com+=1
            print(f"Player={point} and Computer {com}")
        else:
            point+=1
            print(f"Player={point} and Computer {com}")
    elif player=="scissors":
        if computer=="rock":
            com += 1
            print(f"Player={point} and Computer {com}")
        else:
            point += 1
            print(f"Player={point} and Computer {com}")
    else:
        print("Invalid choice")
    if point==5 or com==5:
        break
    computer = random.choice(options)

if com==5:
    print(f"Player={point} and Computer {com}")
    print("You loose Try again latter.....")
else:
    print(f"Player={point} and Computer {com}")
    print("You won Contrangz..........!!!!!")
