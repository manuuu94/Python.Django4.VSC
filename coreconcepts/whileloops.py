#if true it will make loop. add i or it will become infinite
i = 1
while i <= 5:
    print("*"*i)
    i = i + 1
print("done")

#game that allows 3 guesses to pick a name right or you fail
secret_number = 9
i = 0
while i < 3:
    guess = int(input('Guess: '))
    i += 1
    if guess == secret_number:
        print("You won!")
        #i = 4
        #break makes python to terminate the loop
        break
else:
    print("You failed.")

##
command = ""
started = False
#infinite loop with if conditions to get out "break"
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command == "quit":
        print("Ended the program")
        break
    else:
        print("Sorry I don´t understand that")










