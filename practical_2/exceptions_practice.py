finished = False
result = 0
while not finished:
    try:
        entered_number = int(input("Enter an integer: "))
        result = entered_number
        break
    except ValueError:
        print("Please enter a valid integer.")

print("Valid result is:", result)
