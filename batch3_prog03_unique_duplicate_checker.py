#  Create a program that asks the user to input numbers continuously until an invalid input is entered, and displays “Unique” if the number has no duplicate and “Duplicate” if the number has already been entered.

print("="*50, "Program 2".center(50), "="*50, sep="\n")
print("asks the user to input numbers continuously until an invalid input is entered", 
        "and displays “Unique” if the number has no duplicate and “Duplicate” if the number",
        "has already been entered.", "="*50, sep='\n')

number_list = []
while True:
    number = int(input("Please choose a number: "))
    
    if number in number_list:
        print("Duplicate... Please input a unique number")    
    else:
        number_list.append(number)
        print(f"Unique! Current list: {number_list}")