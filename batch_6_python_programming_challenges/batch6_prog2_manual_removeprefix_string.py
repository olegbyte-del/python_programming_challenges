# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

string = input("Please input a string: ")
find_string = input("Please input the part of the string you want to remove: ")

remove_suffix = len(find_string)

if string[:remove_suffix] == find_string:
    format_version = string[remove_suffix:]

print(f"Result: {format_version}")
    