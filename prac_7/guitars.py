from prac_7.guitar import Guitar

print("MY GUITARS!")


def main():
    guitars = []
    add_guitar(guitars)
    for index, guitar in enumerate(guitars):
        print("Guitar {}: {} ({:4}), worth ${:6}".format(index + 1, guitar.name, guitar.year, guitar.cost))


def add_guitar(guitars):
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        new_guitar = Guitar(guitar_name, guitar_cost, guitar_year)
        guitars.append(new_guitar)
        print("{} ({}), worth ${} added!".format(guitar_name, guitar_year, guitar_cost))
        guitar_name = input("Name: ")


main()
