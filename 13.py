# سری فیبوناچی
# راهنمایی : عدد مد نظر از جمع دو عدد قبلی بدست می آید
NUM1 = 1
NUM2 = 2
n = int(input("Please enter number : "))
for i in range(1,n):
    if n == 1 :
        print(NUM1)
    if n == 2 :
        print(i , i+1)
    else : 
        NUM1 = 1
        NUM2 = 2
        i = 3
        while i <= n :
            E3  = NUM1 + NUM2
            print( E3," ")
            NUM1 = NUM2
            NUM2 = E3
            i = i +1     # به i اونقدر ی اضافه میشه تا به n برسه