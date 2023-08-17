import math
print("Please enter the radius :")
Radius = input()   # شعاع ورودی
Area_Circle = ((int(Radius))**2)*(math.pi)*4          #مساحت کره
Volume_Circle = (4/3)*(math.pi)*((int(Radius))**3)    #حجم کره

print("Area Circle :" , Area_Circle)
print("Volume Circle :" , Volume_Circle)
