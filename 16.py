# از کاربر بپرس قراره چند تا عدد وارد کنه و اونارو مرتب کن
N = int(input("How many numbers do you have ? "))
arr = []      # خواندن آرایه
for  i in range(1,N+1):
    # print("Please entrt number " ,i)
     Num=int(input("Please entrt number {}  : ".format(i) ))
     arr.append(Num)

arr.sort(reverse=True)     
print(arr)     
