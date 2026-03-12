# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

string = input("Please input a string: ")

lower = list("abcdefghijklmnopqrstuvwxyz")

status = True
for char in string:
    if char in lower:
        status = False
        break

print(f"Status: {status}")
