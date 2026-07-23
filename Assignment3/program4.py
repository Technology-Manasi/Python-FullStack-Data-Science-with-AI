a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))

if a + b > c and b + c > a and a + c > b:
    print("valid triangle")
else:
    print("Invalid triangle")
    
    
