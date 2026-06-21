n=int(input("enter the number"))

for i in range(2,6):
    if n%2==0:
        print("Not Weird")
    else:
        print("Weird")

for i in range(6,21):
    if n%2==0:
        print("Weird")
    else:
        print("Not Weird")
        
for i in range(21,101):
    if n%2==0:
        print("Not Weird")
    else:
        print("Weird")