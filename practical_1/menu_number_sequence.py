controller = 0
while controller == 0:
    try:
        first_number = int(input("Enter the first number for your sequence: "))
        last_number = int(input("Enter the last number for your sequence: "))
        current_number = first_number
        MENU = """(A) - Show all even numbers from the first number to last number
(S) - Show all odd numbers from the first number to the last number
(D) - Show all squares from the first number to the last number
(Q) - Quit"""
        print(MENU)
        choice = input(">>> ").upper()
        while choice != "Q":
            if choice == "A":
                while current_number <= last_number:
                    if current_number % 2 == 0:
                        print(current_number)
                    current_number += 1
            elif choice == "S":
                while current_number <= last_number:
                    if current_number % 2 != 0:
                        print(current_number)
                    current_number += 1
            elif choice == "D":
                while current_number <= last_number:
                    squared_number = current_number*current_number
                    print(squared_number)
                    current_number += 1
            elif choice == "Q":
                print("See you later!")
                controller = 1
            else:
                print("Not a valid menu input, sorry.")
            second_menu = """(N) - New numbers
(O) - Old Numbers"""
            print(second_menu)
            second_choice = input(">>> ").upper()
            while second_choice != "O":
                if second_choice == "N":
                    first_number = int(input("Enter the first number for your sequence: "))
                    last_number = int(input("Enter the last number for your sequence: "))
                else:
                    print("Assuming old numbers")
                break
            current_number = first_number
            print(MENU)
            choice = input(">>> ").upper()
        break
    except ValueError:
        print("Enter a number, not a letter")
print("See you later!")
