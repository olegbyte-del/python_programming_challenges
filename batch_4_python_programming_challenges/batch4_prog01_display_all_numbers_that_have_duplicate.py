# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

list_number = []
duplicate_number = []
for i in range(10):
    number = int(input("Please input a number: "))
    list_number.append(number)

for num in list_number:
    if list_number.count(num) > 1 and num not in duplicate_number:
        duplicate_number.append(num)
        print([num], end=" ")