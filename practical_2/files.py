user_name = input("Enter your name please: ")
file_with_names = open("name.txt", "w")
print(user_name, file=file_with_names)
file_with_names.close()

file_to_read_from = open("name.txt", "r")
read_name = file_to_read_from.readline()
print("Your name is: ", read_name)
file_to_read_from.close()

number_file = open("numbers.txt", "r")
line_one = int(number_file.readline())
line_two = int(number_file.readline())
result = line_one + line_two
print(result)
number_file.close()

total = 0
number_file = open("numbers.txt", "r")
for line in number_file:
    number = int(number_file.readline())
    total += number
print(total)
number_file.close()
