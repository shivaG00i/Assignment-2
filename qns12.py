# ✨ Question 12  
# Write a program to calculate the
# **product of odd numbers** between 1 and 15 using a **while loop**.

# ---

product = 1
number = 1
while number <= 15:
    if number % 2 != 0:  # Check if the number is odd
        product *= number  # Multiply the product by the odd number
    number += 1  # Increment the number
print(f"Product of odd numbers between 1 and 15: {product}")
