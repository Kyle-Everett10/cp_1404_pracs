from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETERS_RATE = 1.60934


class MilesToKilometersConverter(App):
    def build(self):
        self.title = "Miles to Kilometers converter v1.0"
        self.root = Builder.load_file('converter_layout.kv')
        return self.root

    def real_time_conversion(self, unconverted_number):
        try:
            unconverted_number_int = int(unconverted_number)
            self.root.ids.output_label.text = str(self.handle_conversion(unconverted_number_int))
        except (TypeError, ValueError):
            self.root.ids.output_label.text = str(self.handle_conversion(0))

    def handle_increment(self, increment):
        try:
            unconverted_number = int(self.root.ids.input_number.text)
            self.root.ids.input_number.text = str(unconverted_number + increment)
        except (TypeError, ValueError):
            unconverted_number = 0 + increment
            self.root.ids.input_number.text = str(unconverted_number)
        self.root.ids.output_label.text = str(self.handle_conversion(unconverted_number))

    def handle_conversion(self, value):
        try:
            converted_number = value * MILES_TO_KILOMETERS_RATE
        except (TypeError, ValueError):
            converted_number = 0
        return converted_number


MilesToKilometersConverter().run()
