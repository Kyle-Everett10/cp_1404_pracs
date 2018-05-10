from practical_8.taxi import Taxi


class SilverServiceTaxi(Taxi):
    FLAG_FALL = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = fanciness * super().price_per_km

    def get_fare(self):
        return super().get_fare() + self.FLAG_FALL

    def __str__(self):
        return super().__str__() + "plus flag fall of {}".format(self.FLAG_FALL)
