def fibonacci(num):
    if num==0 or num==1 :
        return num
    else:
        return fibonacci(num - 1 ) + fibonacci(num - 2 )

n=int(input("Enter a number))
print("the fibonacci series ",n,"is",fibonacci(n))
