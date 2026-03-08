# Create a program that asks the user to input numbers continuously until an invalid input is entered, and displays the number with the most duplicates (the number that appears most frequently).

print("="*50, "Program 4".center(50), "="*50, sep="\n")
print("Create a program that asks the user to input numbers continuously", 
        "until an invalid input is entered and displays the",
        "number with the most duplicates (the number that appears most frequently).", "="*50, sep='\n')

number_list = []
most_frequent = None
highest_count = 0

while True:
    try:
        number = int(input("Please input a number: "))
        
        number_list.append(number)
        print("="*50)
        print(f"Current list: {number_list}".center(50))
        print("="*50)
        
        current_num_count = number_list.count(number) # Stores the number of duplicates
        
        if current_num_count > highest_count: # compares the number of duplicate to the highest_count
            highest_count = current_num_count # if its greater it replaces the value of the highest count
            most_frequent = number # the number that was recently input is saved to be the most_frequent
    
    except ValueError:
        print("="*50, "Invalid input!", "="*50, sep="\n")
        print(f"Most Duplicated number: {most_frequent} (Appeared {highest_count} times)", "="*50, sep="\n")