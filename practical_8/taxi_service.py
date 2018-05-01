from practical_8.taxi import Taxi
from practical_8.silverservicetaxi import SilverServiceTaxi

MENU = "q-Quit, c-Choose Taxi, d-Drive Taxi\n Input:"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Hummer", 150, 2), SilverServiceTaxi("Limo", 150, 3)]
    taxi = None
    bill = 0
    user_input = input(MENU)
    while user_input.lower() != "q":
        if user_input.lower() == "c":
            taxi = choose_taxi(taxis)
        elif user_input.lower() == "d":
            if not taxi:
                print("You must choose a taxi first")
            else:
                current_trip = drive(taxi)
                print("Your {} trip cost ${}".format(taxi.car_name, current_trip))
                bill += current_trip
        print("Bill to date: ${}".format(bill))
        user_input = input(MENU)
    print("Total trip cost: ${}".format(bill))
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    print("Taxis available:")
    try:
        display_taxis(taxis)
        taxi_choice = int(input("Choose taxi: "))
        taxi_to_use = taxis[taxi_choice]
        return taxi_to_use
    except (IndexError, ValueError):
        print("Error: Taxi not selected")
        return


def drive(taxi):
    try:
        distance = int(input("Drive how far?: "))
        taxi.drive(distance)
        return taxi.get_fare()
    except ValueError:
        print("Didn't travel at all!")
        return 0


def display_taxis(taxis):
    for index, taxi in enumerate(taxis):
        print("{} - {}\n".format(index, taxi))


main()
