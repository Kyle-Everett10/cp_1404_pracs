from practical_8.silverservicetaxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Prius", 100, 2)
fancy_taxi.drive(18)
print("{} costs ${} to drive 18km (Expected $48.8)".format(fancy_taxi.car_name, fancy_taxi.get_fare()))
