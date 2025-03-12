def swap(a,b):
    return b,a

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
a,b=swap(a,b)
print("The value of a:",a,"The value of b:",b)