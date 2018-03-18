name = input("Enter your name please: ")
MENU = """H -Hello
G - Goodbye
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello {}".format(name))
    elif choice == "G":
        print("Goodbye {}".format(name))
    else:
        print("Not a valid command")
    print(MENU)
    choice = input(">>> ").upper()

print("Finished")
