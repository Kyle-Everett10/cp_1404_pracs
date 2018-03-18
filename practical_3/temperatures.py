"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)


def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            result = temperature_celsius_converter(celsius)
            temperature_format = "F"
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            result = temperature_fahrenheit_converter(fahrenheit)
            temperature_format = "C"
        else:
            print("Invalid option")
        print("{:.2f}{}".format(result, temperature_format))
        print(MENU)
        choice = input(">>> ").upper()


def temperature_celsius_converter(celsius):
    temperature_fahrenheit = celsius+32 * 9/5
    return temperature_fahrenheit


def temperature_fahrenheit_converter(fahrenheit):
    temperature_celsius = 5/9 * (fahrenheit - 32)
    return temperature_celsius


main()
print("Thank you.")
