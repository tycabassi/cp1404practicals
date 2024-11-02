from prac_06.programming_languages import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
languages = [python, ruby, visual_basic]
for language in languages:
    print(language)

print("The languages which are dynamically typed are: ")
for language in languages:
    if language.is_dynamic():
        print(language.name)
