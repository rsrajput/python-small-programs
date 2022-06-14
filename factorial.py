def factorial(n    ):
    return 1 if n <=1 else n*factorial(n-1)

num = int(input("enter a num"))

print("factorial", factorial(num))
