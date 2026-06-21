n = int(input("enter the number"))
l=len(str(n))
rev = 0
temp=n
while(n!=0):
    r=n % 10
    rev = (rev * 10) + r
    n = n//10

if rev == temp:
    print("palindrome")
else:
    print("not palindrome")