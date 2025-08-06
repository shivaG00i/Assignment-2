# ✨ Question 5  
# Write a program that prints all
# **2-digit numbers** whose sum of digits is exactly **10**.  
# (Example: 19 → 1 + 9 = 10)

for i in range(10, 100):
    str1 = str(i)
    sum1 = int(str1[0]) + int(str1[1])
    if sum1 == 10:
        print(i)


