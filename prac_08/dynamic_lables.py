from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """Turns names from a list into Labels"""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Greg", "Sam", "John", "Jane"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_label()
        return self.root

    def create_label(self):
        """Add a label which gets the names from a list."""
        print("Showing Label form")
        for name in self.names:
            name_label = Label(text=f"Name: {name}")
            self.root.add_widget(name_label)


DynamicLabelApp().run()
