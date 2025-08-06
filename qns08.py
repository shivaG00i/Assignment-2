# ✨ Question 8  
# Write a program to create a **right-angled triangle** 
# using a character entered by the user.

# Example:
# ```
# Enter character: $
# Output:
# $
# $$
# $$$
# $$$$
# ```


# char = input("Enter character: ")
# for i in range(1, 6):
#     print(char * i)  # Print the character 'i' times for each row
    
# or

char1 = input("Enter character: ")

for i in range(1,5):
    for j in range(i):
        print(char1, end=' ')
    print()