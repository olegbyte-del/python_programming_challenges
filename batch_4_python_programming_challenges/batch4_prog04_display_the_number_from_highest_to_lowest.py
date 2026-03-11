# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

number_list = []

while True:
    try:
        number = int(input("Please input a number: "))
        number_list.append(number)
        
        number_list.sort(reverse=True)
    except ValueError:
        break

print(number_list, end=" ")