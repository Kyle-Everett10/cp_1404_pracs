class ProgrammingLanguage:

    def __init__(self, language_name, typing, reflection, year):
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} typing, Reflection = {}, First appeared in {}".format(self.language_name, self.typing,
                                                                             self.reflection, self.year)
