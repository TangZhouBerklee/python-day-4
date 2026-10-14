menu = {
    "Burger": 12,
    "Pizza": 10,
    "Salad": 8
}

for item in menu:
    print(item + ": $" + str(menu[item]))

choice = input("Choose an item: ")

if choice in menu:
    print("$" + str(menu[choice]))
else:
    print("Item not on the menu.")