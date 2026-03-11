# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

num1 = int(input("Please input a number: "))
num2 = int(input("Please input a number: "))

result = num1 ** num2

print(f"{num1} raised to {num2} is equal to: {result}")