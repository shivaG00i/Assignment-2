# ✨ Question 13  
# Write a program that reverses a number using a
# **while loop** without using str() or reversed().

# Example:  
# Input: 1234  
# Output: 4321

rev=0
num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10  # Get the last digit
    rev = rev * 10 + digit  # Build the reversed number
    num //= 10  # Remove the last digit from the original number
print(f"Reversed number: {rev}")
