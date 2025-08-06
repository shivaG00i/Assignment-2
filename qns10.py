# ✨ Question 10  
# Write a program that prints all numbers between 1 and 500
# that are divisible by **7** or **11**.

for number in range(1, 501):
    if number % 7 == 0 or number % 11 == 0:
        print(number, end=' ')