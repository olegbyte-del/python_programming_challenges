# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

list_numbers = []
for i in range(10):
    try:
        number = int(input("Please input a number: "))
        list_numbers.append(number)
    except ValueError:
        print("Invalid Input. Please enter an integer number.")
        