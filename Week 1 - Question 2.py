x = int(input("Please input a number that you would like to know the factorial of: "))

factorial = 1

for i in range(1, x+1):
    factorial = factorial * i
    print(factorial, end = ', ')
