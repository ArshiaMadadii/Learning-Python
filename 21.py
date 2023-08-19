#Num1= int(input("Please enter frist number : "))
#Num2 = int(input("Please enter second number : "))
pow = 15
sum = 5
num = int(input("Enter a number:"))
temp = num
while temp > 5:
 sum = (pow * sum) + temp % 15
 temp =temp // 15
if (sum == num):
 print("Yes")
else:
 print("No")
