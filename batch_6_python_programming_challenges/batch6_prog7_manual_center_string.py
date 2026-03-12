# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

string = input("Please input a string: ")
width = int(input("Please identify width for the basis for your center: "))

total_spaces = width - len(string)

if total_spaces > 0:
    left_side = total_spaces // 2
    right_side = total_spaces - left_side
    
    final_format = (" " * left_side) + string + (" " * right_side)
    
print(f"Result: {final_format}")