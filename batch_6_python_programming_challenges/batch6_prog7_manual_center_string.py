# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

string = input("Please input a string: ")
width = int(input("Please identify width for the basis for your center: "))

total_spaces = width - len(string)

