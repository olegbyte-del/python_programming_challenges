# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

number_list = []

for i in range(100):
    number = int(input("Please input a number: "))
    number_list.append(number)
    
    number_list.sort()

for num in number_list:
    print([num], end=" ")