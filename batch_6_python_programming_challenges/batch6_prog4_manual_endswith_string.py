# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

string = input("Please input a string: ")
find_string = input("Please identify the part of the string you want to check: ")

find_string_len = len(find_string)

if string[-find_string_len:] == find_string:
    status = True
else:
    status = False 
print(f"Result: {status}")