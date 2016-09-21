import random

while True:
    ask_user = input("Would you like to roll the dice?: yes/y or no/n\n")
    if ask_user in ("yes", "y"):
        print(random.randint(1,6))
        print("Congrats you rolled the dice! Let's keep doing it forever and ever and ever...\n")
    elif ask_user in ("no", "n"):
        print("You must press 'yes' or 'y'\n")
