#Area of Rectangle
length=int(input("Enter Length:"))
breadth=int(input("Enter Breadth:"))

def rectangle_area(length,breadth):
    area=length*breadth
    return area

result=rectangle_area(length,breadth)
print("Area of Rectangle:",result)
