# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

string = input("Please input a string: ")
find_string = input("Please identify what string to find: ")

status = True

if find_string in string:
    pass
else: 
    status = False

print(f"Status: {status}")