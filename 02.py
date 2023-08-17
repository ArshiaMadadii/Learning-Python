import math
print("Please enter the radius :")   # شعاع ورودی
Radius = input()
print("Please enter the height :")   # ارتفاع ورودی
height = input()
cylinder_volume = (int(height))*(int(Radius)**2)*(math.pi)     # حجم ورودی
area_of_the_cylinder = ((2*(math.pi))*(int(Radius))*(int(height)))+(2*((math.pi)*(int(Radius)**2)))    #مساحت ورودی
print("Cylinder volume :" ,cylinder_volume )
print("Area of the cylinder :" , area_of_the_cylinder )
print((int(height))*(int(Radius)^2)*(math.pi))