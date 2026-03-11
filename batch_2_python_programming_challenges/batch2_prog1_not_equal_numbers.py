# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

num1 = int(input("Please input a number: "))
num2 = int(input("Please input a number: "))

if num1 > num2:
    print(f"The smaller number is: {num2}")
else:
    print(f"The smaller number is: {num1}")