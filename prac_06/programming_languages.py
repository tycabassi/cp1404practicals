"""Estimated time: 20-25 minutes
Actual time: """


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        self.typing = "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

# language_type = input("Enter the type of programming language:")
# reflected = input("What type of reflection is the language?(Dynamic)(Static)").title()
# year = input("Enter a year")
#
# programming_language = ProgrammingLanguage(name, language_type, reflected, year)
