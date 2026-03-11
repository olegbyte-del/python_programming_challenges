# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

number_list = []
unique_list = []

for i in range(10):
    number = int(input("Please input a number: "))
    number_list.append(number)
    
for num in number_list:
    if num not in unique_list:
        unique_list.append(num)
        
print(unique_list)