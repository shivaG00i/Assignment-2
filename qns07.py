# ✨ Question 7  
# Write a program to print all **palindrome numbers**
# between 100 and 200.  
# (A number is a palindrome if it reads the same backward.)


for i in range(100,201):
    pal=str(i)
    if pal==pal[::-1]:
        print(pal)