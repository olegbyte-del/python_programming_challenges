# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

string = input("Please input a string: ")
width = int(input("Please identify the width: "))

space_needed = width - len(string)

if space_needed > 0: 
    final_format = string + " " * space_needed

print(f"Result: {final_format}")