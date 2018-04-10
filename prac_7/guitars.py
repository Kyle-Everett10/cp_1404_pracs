from prac_7.guitar import Guitar
print("MY GUITARS!")


def main():
    index = 1
    guitars = add_guitar()
    for guitar in guitars:
        print("Guitar {}: {} ({:4}), worth ${:6}".format(index, guitar.name, guitar.year, guitar.cost))
        index += 1


def add_guitar():
    guitars = []
    guitar_name = input("Name: ")
    if guitar_name == "":
        return guitars
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $"))
    new_guitar = Guitar(guitar_name, guitar_cost, guitar_year)
    guitars.append(new_guitar)
    print("{} ({}), worth ${} added!".format(guitar_name, guitar_year, guitar_cost))
    while guitar_name != "":
        guitar_name = input("Name: ")
        if guitar_name == "":
            return guitars
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        new_guitar = Guitar(guitar_name, guitar_cost, guitar_year)
        guitars.append(new_guitar)
        print("{} ({}), worth ${} added!".format(guitar_name, guitar_year, guitar_cost))


main()
