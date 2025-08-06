# ✨ Question 11  
# Write a program to print this pattern (numeric pyramid):
# # ```
#     1
#   1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
# ```


for i in range(1, 6):
    # Print leading spaces
    print(' ' * (5 - i), end=' ')
    # Print numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=' ')
    print()  # Move to the next line after each row