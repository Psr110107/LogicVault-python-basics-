l=[]
n = int(input(" enter the number:--> "))

for i in range(n):
    l.append(int(input("ENTER  THE ELEMENTS")))


sum_even=0
sum_odd=0

5
for j in l:
        if j % 2 ==0:
            sum_even+= j
        else:
            sum_odd+=j

print(sum_even)
print(sum_odd)
print(l)

if(n%2==0):
    print("even")
else:
    print("odd")

