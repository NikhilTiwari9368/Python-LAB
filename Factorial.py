def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
n=5
print("Factorial of ",n,"is",factorial(n))