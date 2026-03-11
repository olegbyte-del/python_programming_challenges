# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

string = input("Enter text: ")
target_char = input("Enter character to find: ")

position = -1

for i in range(len(string)):
    if string[i] == target_char:
        position = i
        break

