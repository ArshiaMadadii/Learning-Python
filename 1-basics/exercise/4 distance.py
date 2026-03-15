import math
a = (3,4)
b = (0,0)
y1 ,x1= a[0],a[1]
y0,x0 = b[0],b[1]

distance = (y1 - y0)**2 + (x1-x0)**2
distance = math.sqrt(distance)
print(distance)