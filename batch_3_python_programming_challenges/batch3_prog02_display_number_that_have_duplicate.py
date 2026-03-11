# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

number_list = []

for i in range(10):
    number = int(input("Please input a number: "))
    
    number_list.append(number)