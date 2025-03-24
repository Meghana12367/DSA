#factorial of a number

num = int(input("Enter the number:"))
factorial = 1 #The variable factorial is initialized to 1 because the multiplication of numbers starts with 1
if num < 0:
    print("Factorial doesn't exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num):
        factorial = factorial*i
    print("The factorial of", num, "is", factorial)