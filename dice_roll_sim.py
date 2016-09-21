import random

#while True:
#    print random.randint(1,6)
"""
while True:
    ask_user = raw_input("Would you like to roll the dice?")
    if ask_user == "yes" or "y":
        print random.randint(1,6)
    else: ask_user == "no" or "n":
        print("Just roll the dye already")
"""

ask_user = raw_input("would you like to roll the dice?")
if ask_user == "yes" or "y":
    print random.randint(1,6)
else ask_user != "yes" or "y":
    print("You're wasting my time")
