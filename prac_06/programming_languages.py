"""Estimated time: 20-25 minutes
Actual time: """


class ProgrammingLanguage:
    def __init__(self, typing="", reflection="", year=""):
        self.typing = typing
        self.reflection = reflection
        self.year = year


language_type = input("Enter the type of programming language:")
reflected = input("Is it reflected?")
year = input("Enter a year")

programming_language = ProgrammingLanguage(language_type, reflected, year)
