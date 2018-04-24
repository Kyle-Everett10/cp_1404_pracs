from prac_7.programming_language import ProgrammingLanguage
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
if python.is_dynamic():
    print("Is dynamic")
if not visual_basic.is_dynamic():
    print("Is not dynamic")
languages = [ruby, python, visual_basic]
print("The dynamic languages are: ")
for language in languages:
    if language.is_dynamic():
        print(language.language_name)
