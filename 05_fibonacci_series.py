def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-2) + fib(n-1)

n = int(input("enter the number"))
for i in range(0,n):
    print(fib(i))
print(fib(n))