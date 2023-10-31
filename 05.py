# تام
Numb = int(input())
array=[]
for i in range(1,Numb) :
    if Numb%i == 0 :
         array.append(i)
#print(array)
total =sum(array)
#print(total)
if total == Numb :
    print("YES") 
    
else :
    print("NO")                 