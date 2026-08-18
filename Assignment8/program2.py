#Area of Circle
import math

radius=int(input("Enter radius:"))

def circle_area(radius):
    area=math.pi*radius*radius
    return area
result=circle_area(radius)
print("Area of circle:",result)
