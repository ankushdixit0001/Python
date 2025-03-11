a=float(input("Enter the side a:"))
b=float(input("Enter the side b:"))
c=float(input("Enter the side c:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**(0.5)
print("area of triangle:",area)