import math

def isPerfectSquare(x):
    s=int(math.sqrt(x))
    return s*s == x

def isFib(n):
    return isPerfectSquare(5*n*n +4) or isPerfectSquare(5*n*n -4)

for i in range(1,50):
    if (isFib(i) == True):
        print(i, "is a Fibonacci")
    # else:
    #     print(i, " is not a Fib")
