from practical_8.unreliable_car import UnreliableCar

car_1 = UnreliableCar("Falcon", 100, 50)
if car_1.drive(50) > 0:
    print("Drove successfully")
else:
    print("Not again!")

car_2 = UnreliableCar("Commodore", 100, 50)
if car_2.drive(50) > 0:
    print("I knew it")
else:
    print("Wow, didn't expect this")
