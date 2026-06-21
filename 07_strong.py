n = int(input("enter the number"))
sum = 0
temp = n
while(n!=0):
    fact=1
    r=n%10
    for i in range(2,r+1):
        fact*=i
    sum =sum + fact
    n = n//10

if sum == temp:
    print("strong number")
else:
    print("not a strong number")