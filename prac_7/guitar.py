class Guitar:

    def __init__(self, name="", cost=0, year=0):
        self.name = name
        self.cost = cost
        self.year = year

    def __str__(self):
        return "{} ({}): ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2018-self.year

    def is_vintage(self, age):
        if age >= 50:
            return True
        else:
            return False
