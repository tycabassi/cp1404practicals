from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Make a Box layout which lets the user type in a name and clear it if needed."""
    def build(self):
        """Creates Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handles what occurs after greet button is pushed."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handles what occurs after clear button is pushed."""
        self.root.ids.output_label.text = f"Enter your name"
        self.root.ids.input_name.text = " "


BoxLayoutDemo().run()
