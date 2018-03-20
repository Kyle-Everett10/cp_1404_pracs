import random
number_of_lines = int(input("Enter how many quick picks you want: "))
number = 0
for lines in range(0, number_of_lines):
    numbers = []
    list_has_values = False
    for current_number in range(0, 6):
        new_number = random.randrange(1, 45)
        if list_has_values is True:
            for number in numbers:
                test = number
                while len(numbers) != current_number:
                    while new_number == number:
                        new_number = random.randrange(1, 45)
                    if new_number > number:
                        numbers.insert(, new_number)
                    elif new_number < number:
                        numbers.insert(, new_number)
                    break
        else:
            numbers.append(new_number)
            list_has_values = True
    print(numbers)
