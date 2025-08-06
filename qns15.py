# ✨ Question 15  
# Write a program that asks for 10 integers and  
# then prints how many were **positive**, **negative**, and **zero**.

zero=0
positive=0
negative=0
for i in range(10):
    num = int(input("Enter an integer: "))
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
print(f"Positive numbers: {positive}, Negative numbers: {negative}, Zeros: {zero}")