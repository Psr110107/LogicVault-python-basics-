with open("python.txt","w") as f:
    f.write("hello world")

with open("python.txt","r") as f:
    print(f.read())