history = []

while True:
    command = input("Enter command: ")
    if command == "history":
        for i in range(len(history)):
            print(i + 1, history[i])

    elif command == "exit":
        break

    else:
        history.append(command)
        print("Command logged.")