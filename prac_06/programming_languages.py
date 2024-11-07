"""Estimated time: 20-25 minutes
Actual time: 31 minutes"""


class ProgrammingLanguage:
    """Store information about a programming language sorting them if they are dynamic or not."""
    def __init__(self, name="", typing="", reflection="", year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns true if the language is dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Returns a string representation of the language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"


