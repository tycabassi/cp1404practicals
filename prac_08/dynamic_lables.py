from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelApp(App):
    """Turns names into"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.name_to_age = {"Greg": 40, "Sam": 78, "John": 54, "Jane": 13}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_label()
        # self.create_widgets()
        return self.root

    def create_label(self):
        """Add a label to the Kivy GUI."""
        print("Showing Label form")
        for name in self.name_to_age:
            name_label = Label(text= f"Name: {name}")
            contact_label = Label(text=f"Age:{self.name_to_age[name]}")
            self.root.add_widget(name_label)
            self.root.add_widget(contact_label)


DynamicLabelApp().run()
