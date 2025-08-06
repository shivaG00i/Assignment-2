# ✨ Question 9  
# Write a program that asks the user to enter numbers 
# until they enter `0`,  
# then prints the **total sum** and **average** of
# all entered numbers.

list_of_numbers = []

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    list_of_numbers.append(number)
    
total_sum = sum(list_of_numbers)
average = total_sum / len(list_of_numbers) if list_of_numbers else 0
print(f"Total sum: {total_sum}", "Average: {average}")

