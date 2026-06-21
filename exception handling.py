try:
    a=int(input("enter no"))
    b=int(input("enter no.2"))

    print("division ",a/b)

except ZeroDivisionError:
    print("cannt be divided")

finally:
    print("done")