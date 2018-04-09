from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NameLister(App):
    def __init__(self):
        super().__init__()
        self.names = ["Kyle", "James", "Jackson"]

    def build(self):
        self.title = "Name Lister"
        self.root = Builder.load_file("name_lister_layout")
        self.display_names()
        return self.root

    def display_names(self):
        for name in self.names:
            temp_label = Label(id=name, text=name)
            self.root.ids.name_box.add_widget(temp_label)


NameLister().run()
