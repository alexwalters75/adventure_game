import time
import random

backpack = []

baddie = ["Vinz Clortho The Keymaster", "Zuul The Gatekeeper",
        "Stay Puft the Marshmallow Man",
        "Gozer The Destroyer", "Vigo The Carpathian"]

random_baddie = random.choice(baddie)

def print_pause(message):
    print(message)
    time.sleep(1)

def intro():
    print_pause("\n"
                "'It\'s right here!', screams Egon.\n")
    print_pause("The Ectomobile screeches to a halt in front of City Hall "
                "and the four of you run through the front door.\n")
    print_pause("'I really hate tall buldings' moans Venkman\n")
    print_pause("Your stomach sinks as you realise that you have left the "
                "ghost trap in the car\n")
    print_pause("'Guys, I think we have a bit of a problem....'\n")
    print_pause("'There's no time and we have to get to the roof' insists Egon")
    print_pause("'The elevator is broken so we have to take the stairs!!'\n")

intro()

while True:
    print_pause("\n"
                "What would you like to do?")
    print_pause("Enter 1 to head back to the car")
    print_pause("Enter 2 run up the stairs")
    option1 = input("Please enter 1 or 2\n")
    if option1 == '1':
        print_pause("You run back out the doors and scramble through the "
                    "rubbish in the boot of the ectomobile")
        if "ghost_trap" in backpack:
            print_pause("You already have the ghost trap")
            print_pause("You hurry back up to City Hall and run "
                        "back into the lobby at the bottom of "
                        "the stairs")
        else:
            print_pause("You pick up the ghost trap")
            backpack.append("ghost_trap")
            print_pause("You hurry back up to City Hall and run "
                        "back into the lobby at the bottom of "
                        "the stairs\n")
    elif option1 == '2':
        print_pause("You run up 25 flights of stairs and "
                    "reappear on the roof")
        print_pause(f"'Holy moly, its {random_baddie}!'")
        print_pause("\n"
                    "What would you like to do?\n")
        print_pause("Enter 1 to fight to the death")
        print_pause("Enter 2 run back down the stairs")
        option2 = input("Please enter 1 or 2\n")
        if option2 == '1':
            print_pause("You start fighting")
            if "ghost_trap" in backpack:
                print_pause("You have the ghost trap")
                print_pause("You kill the baddie\n")
                play_again = input("Would you like to play again?\n"
                                   "Please enter y or n\n").lower()
                if play_again == 'y':
                    print_pause("OK great, let me load that back up for you")
                    exit()
                else:
                    print_pause("No problem - hope you enjoyed the game!")
                    exit()
            else:
                print_pause("You don't have the ghost trap")
                print_pause("You are defeated by the baddie")
                play_again = input("Would you like to play again?\n"
                                   "Please enter y or n\n").lower()
                if play_again == 'y':
                    print_pause("OK great, let me load that back up for you")
                    exit()
                else:
                    print_pause("No problem - hope you enjoyed the game!")
                    exit()
        elif option2 == 2:
            print_pause("You run back down to the lobby")
