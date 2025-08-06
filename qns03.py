# ✨ Question 3  
# Write a program to print the following pattern
# using **nested loops**:
# ```
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# ```


for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=' ')
    print()  # Move to the next line after each row