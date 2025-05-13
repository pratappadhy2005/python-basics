name = input("Enter your name: ")
print("Hello ", name, "welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "y" or should_we_play == "yes":
    print("Let's play!")

    direction = input("Do you want to go left or right: ").lower()
    if direction == "left":
        print("Okay we will go left: ")
    elif direction == "right":
        print("Okay we will go right: ")
        choice = input("Do you want to go up or down: ").lower()
        if choice == "up":
            print("You fell into a hole. Game over!")
        elif choice == "down":
            print("You fell into a hole. Game over!")
        else:
            print("We went to the wrong direction")
    else:
        print("We went to the wrong direction")
else:
    print("Ok, maybe next time.")
