import images
import os

dresserOpened = False
hasKey = False

while True:
    print(images.middle)
    direction = input("> ").lower()
    if direction == 'r':
        if dresserOpened:
            print(images.dresserOpened) #
            input("> ")
        else:
            while True:
                print(images.dresserClosed)
                password = input("> ").lower()
                if password == "lost":
                    dresserOpened = True
                    hasKey = True
                    print(images.dresserOpen)
                    input("> ")
                    break
                if not password:
                    break

    elif direction == 'l':
        print(images.painting)
        input("> ")
    elif direction == 'f':
        print(images.doorClosed)
        input("> ")
        if hasKey:
            print(images.doorOpen)
            input("> ")
            print(images.complete)
            input("> ")
            break
