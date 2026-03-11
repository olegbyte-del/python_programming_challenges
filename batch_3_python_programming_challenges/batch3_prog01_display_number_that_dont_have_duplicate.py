# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

number_list = []

for i in range(10):
    number = int(input("Please input a number: "))
    
    number_list.append(number)
    

check_duplicate = number_list.count()
print(check_duplicate)
