# og01: Create a program that ask user to input 2 numbers. Print the bigger number.


num1 = int(input("Please input a number: "))
num2 = int(input("Please input a number: "))

if num1 > num2:
    print(f"The bigger number is {num1}")
elif num2 > num1:
    print(f"The bigger number is {num2}")
else:
    print("Invalid Input!")

