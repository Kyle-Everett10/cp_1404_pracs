from practical_8.car import Car
from random import randrange


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        chance_to_drive = randrange(0, 101)
        if chance_to_drive >= self.reliability:
            distance = 0
        super().drive(distance)
        return distance

