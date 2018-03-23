import random


def main():
    number_of_lines = int(input("Enter how many quick picks you want: "))
    for lines in range(0, number_of_lines):
        print(generate_line())


def generate_line():
    numbers = []
    list_has_values = False
    for current_number in range(0, 6):
        new_number = random.randrange(1, 45)
        if list_has_values is True:
            returned_index, returned_number = number_index_checker(new_number, numbers)
            numbers.insert(returned_index, returned_number)
        else:
            numbers.append(new_number)
            list_has_values = True
    return numbers


def number_index_checker(new_number, numbers):
    index = 0
    checked_lines = 0
    for NUMBER in numbers:
        while new_number == NUMBER:
            new_number = random.randrange(1, 45)
    while checked_lines != len(numbers):
        if new_number > numbers[index]:
            index += 1
            checked_lines += 1
        elif new_number < numbers[index]:
            return index, new_number
    return index, new_number


main()
