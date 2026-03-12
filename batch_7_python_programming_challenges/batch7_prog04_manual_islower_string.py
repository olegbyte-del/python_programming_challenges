# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

string = input("Please input a string: ")

lower = list("abcdefghijklmnopqrstuvwxyz")

status = None

for char in range(len(string)):
    try:
        if char in lower:
            status = "True"
        else:
            status = "False"
    except ValueError:
        print("Invalid input!")

print(status)