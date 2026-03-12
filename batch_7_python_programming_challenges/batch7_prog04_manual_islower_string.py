# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

string = input("Please input a string: ")

lower = list("abcdefghijklmnopqrstuvwxyz")

status = True

for char in string:
    try:
        if char in lower:
            pass
        else:
            status = False
    except ValueError:
        print("Invalid input!")

print(status)