"""Kyle"""
name = input("Enter your name here: ")
while name == "":
    print("Not a valid name")
    name = input("Enter your name here: ")
for character in range(0, len(name), 2):
        print(name[character])

print("Done")
