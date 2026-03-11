# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

name = input("Please inpu your name: ").lower()

snake_case_format = name.replace(" ", "_")

print(f"The snake version of: {name} is {snake_case_format}")