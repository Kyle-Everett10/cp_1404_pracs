from kivy.app import App
from kivy.lang import Builder


class MilesToKilometersConverter(App):
    def build(self):
        self.title = "Miles to Kilometers converter"
        self.root = Builder.load_file('converter_layout.kv')
        return self.root

    def handle_increment(self, increment):
        try:
            self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + increment)
        except TypeError:
            self.root.ids.input_number.text = str(0+increment)
        except ValueError:
            self.root.ids.input_number.text = str(0+increment)

    def handle_conversion(self, value):
        try:
            local_value = int(value)
            self.root.ids.output_label.text = str(local_value * 1.60934)
        except TypeError:
            local_value = 0
            self.root.ids.output_label.text = str(local_value)
        except ValueError:
            local_value = 0
            self.root.ids.output_label.text = str(local_value)


MilesToKilometersConverter().run()
