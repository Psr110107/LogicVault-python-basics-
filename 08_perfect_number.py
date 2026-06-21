n = int(input("ENTER THE NUMBER"))
sum = 0
temp = n
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
    else:
        continue
if(temp==sum):
    print("the number is perfect")
else:
    print("the number is not perfect")
            