import Graphics
from Graphics import circle, rectangle
from Graphics.threeGraphics import cuboid, sphere
from Graphics.circle import *
rad1 = float(input("enter the radius of the circle:"))
print("area of circle is:", circle.area_circle(rad1))
print("perimeter of circle is:",)
circle.perimeter_circle((rad1))
len1 = float(input("enter the length of the rectangle:"))
breadth1 = float(input("enter the breadth of the rectangle:"))
print("area of rectangle is:", rectangle.area_rec(len1,breadth1))
print("perimeter of rectangle is:", rectangle.perimeter_rec(len1, breadth1))
len2 = float(input("enter the length of the cuboid: "))
breadth2 = float(input("enter the breadth of the cuboid: "))
height = float(input("enter the height of the cuboid: "))
print("area of cuboid is:", cuboid.area_cuboid(len2, breadth2, height))
rad2 = float(input("enter the radius of the sphere: "))
print("area of the sphere is", sphere.area_sphere(rad2))
print("perimeter of sphere is:", sphere.perimeter_sphere(rad2))
