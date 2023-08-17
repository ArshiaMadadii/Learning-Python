#سه تا عدد بگیره به ترتیب  پس بده
a = int(input("Please enter frist number : "))
b= int(input("please enter seconed number : "))
c = int(input("please enter Third number : "))
# if a > b > c :
#     print ( a , b ,  c )
    
# elif a > c > b :
#        print ( a , c , b )
# elif c > b > a :
#     print ( c , b ,  a )
    
# elif c > a > b :
#        print ( c , a ,  b )
       
# elif b > c > a :
           
#     print ( b ,  c  , a )  
    
# elif b > a > c :
#     print ( b , a ,  c )     
    
# else :
#     print("ERRORE")
    
    
    # دنبال یه تابع برای راحت تر کردن کار  
    # به نظرت باید چی کار کرد؟
    # استفاده از تابع ثورتد میتونه کمک کننده باشه
num = (a,b,c)          # اول مقادیر رو توی نام میریزم
Snum = sorted(num)     # مرتب شده نام رو در ثنام میرزم 
print(Snum)            # حالا کافیه که پرینتش بگیرم