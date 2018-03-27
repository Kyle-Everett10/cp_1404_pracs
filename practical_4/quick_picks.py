import random
MIN_NUMBER = 1
MAX_NUMBER = 25
NUMBERS_PER_LINE = 6


def main():
    number_of_lines = int(input("Enter how many quick picks you want: "))
    for lines in range(0, number_of_lines):
        print(generate_line())


def generate_line():
    numbers = []
    for i in range(0, NUMBERS_PER_LINE):
        new_number = random.randrange(MIN_NUMBER, MAX_NUMBER)
        while new_number in numbers:
            new_number = random.randrange(MIN_NUMBER, MAX_NUMBER)
        numbers.append(new_number)
    numbers.sort()
    return numbers

main()
