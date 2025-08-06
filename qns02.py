# ✨ Question 2  
# Write a program that finds the **largest number** 
# entered by the user.  
# Ask the user to **enter 7 numbers**,
# use a **for loop**, and print the largest.


largest = None
for i in range(7):
    number = int(input("Enter a number: "))
    if i == 0:
        largest = number
    else:
        if number > largest:
            largest = number
print("The largest number is:", largest)

# or

list1 = []
for i in range(7):
    number = int(input("Enter a number: "))
    list1.append(number)
max1 = max(list1)
print("The largest number is:", max1)
