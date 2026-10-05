# Activity 6

state = "coding"

while True:
    if state == "coding":
        print("You are coding!")
        while True:
            feeling = input("Are you feeling tired, hungry, or happy: ")
            feeling = feeling.lower()
            if feeling == "tired":
                state = "sleeping"
                break
            elif feeling == "hungry":
                state = "eating"
                break
            elif feeling == "happy":
                state = "coding"
                break
            else:
                print("Invalid feeling")

    elif state == "eating":
        print("You are eating!")
        while True:
            feeling = input("Are you feeling hungry, full, or tired: ")
            feeling = feeling.lower()
            if feeling == "hungry":
                state = "eating"
                break
            elif feeling == "full":
                state = "coding"
                break
            elif feeling == "tired":
                state = "sleeping"
                break
            else:
                print("Invalid feeling")

    elif state == "sleeping":
        print("You are sleeping!")
        while True:
            feeling = input("Are you feeling hungry, awake, or tired: ")
            feeling = feeling.lower()
            if feeling == "hungry":
                state = "eating"
                break
            elif feeling == "awake":
                state = "coding"
                break
            elif feeling == "tired":
                state = "sleeping"
                break
            else:
                print("Invalid feeling")
