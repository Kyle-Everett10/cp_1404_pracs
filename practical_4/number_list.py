current_input = 0
MAXIMUM_INPUTS = 5
numbers = []
while current_input < MAXIMUM_INPUTS:
    number = int(input("Enter a number: "))
    numbers.append(number)
    current_input += 1
print("The first number is: {}".format(numbers[0]))
print("The last number is: {}".format(numbers[-1]))
print("The smallest number is: {}".format(min(numbers)))
print("The largest number is: {}".format(max(numbers)))
print("The average of the numbers is: {}".format(sum(numbers)/len(numbers)))
