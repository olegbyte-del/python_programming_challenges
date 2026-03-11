# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

name = input("Please enter your fullname: ").lstrip()

print(f"Your name is: {name}")

