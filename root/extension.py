state = "home"

while True:
    if state == "home":
        print("You are at home.")
        while True:
            choice = input("Where do you want to go? school, park, store: ")
            choice = choice.lower()
            if choice == "school":
                state = "school"
                break
            elif choice == "park":
                state = "park"
                break
            elif choice == "store":
                state = "store"
                break
            else:
                print("Invalid choice")

    elif state == "school":
        print("You are at school.")
        while True:
            choice = input("Where do you want to go? home, park, store: ")
            choice = choice.lower()
            if choice == "home":
                state = "home"
                break
            elif choice == "park":
                state = "park"
                break
            elif choice == "store":
                state = "store"
                break
            else:
                print("Invalid choice")

    elif state == "park":
        print("You are at the park.")
        while True:
            choice = input("Where do you want to go? home, school, store: ")
            choice = choice.lower()
            if choice == "home":
                state = "home"
                break
            elif choice == "school":
                state = "school"
                break
            elif choice == "store":
                state = "store"
                break
            else:
                print("Invalid choice")

    elif state == "store":
        print("You are at the store.")
        while True:
            choice = input("Where do you want to go? home, school, park: ")
            choice = choice.lower()
            if choice == "home":
                state = "home"
                break
            elif choice == "school":
                state = "school"
                break
            elif choice == "park":
                state = "park"
                break
            else:
                print("Invalid choice")