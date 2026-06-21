n = int(input("ENTER THE NUMBER"))
l=len(str(n))
sum=0
temp=n
while(n!=0):
    r = n%10
    sum = sum + r**l
    n=n//10
if sum == temp:
    print("NUMBER IS ARMSTRONG")
else:
    print("NOT AN ARMSTRONG NUMBER")