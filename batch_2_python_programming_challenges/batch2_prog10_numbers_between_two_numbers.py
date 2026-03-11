# Create a program that asks the user to input two numbers and then prints all numbers between the two inputs.

print("="*50, "Program 2".center(50), "="*50, sep="\n")
print("asks the user to input two numbers", 
        "and then prints all numbers between the two inputs.", "="*50, sep='\n')

num1 = int(input("Please choose a number: "))
num2 = int(input("Please choose a number: "))

for i in range(num1 + 1, num2):
        print([i], end=" ")