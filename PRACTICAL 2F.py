import math
length = float(input("enter rectangle length:"))
breadth = float(input("enter rectangle breadth:"))
area_rect = length * breadth
perimeter_rect = 2 *(length + breadth)

radius = float(input("enter circle radius:"))
area_circle = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print("\nrectangle",area_rect)
print("\nrectangle",perimeter_rect)
print("\nrectangle",area_circle)
