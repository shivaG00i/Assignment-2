# ✨ Question 14  
# Write a program to print all prime numbers from 2 to 50 using a **nested for loop**.

for num in range(2, 51):
    is_prime = True  # Assume the number is prime
    for i in range(2, int(num**0.5) + 1):  # Check divisibility from 2 to sqrt(num)
        if num % i == 0:  # If num is divisible by i, it's not prime
            is_prime = False
            break  # No need to check further
    if is_prime:
        print(num, end=' ')  # Print the prime number