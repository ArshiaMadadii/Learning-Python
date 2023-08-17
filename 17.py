# تعداد سال های پیشبنی و ارزش فعلی و نرخ تورم آتی رو بگیره و بوجه پیشنهادی رو اعلام کنه
# نیاز به آرایه برای گرفتن تعدا سال ورودی و نیاز به حلقه فور برای انجام عملات

price = int(input("Please enter price : ") )
inc = int(input("Please enter inc : "))
year = int(input("Please enter years : "))

arr = []
for i in range(1,year+1):
    price = ((inc* price)/100)+price
    arr.append(price)
    print("Cost of the year ", i ," : ", price)
budget=sum(arr)
print("Budget required : " , budget )     
    
    
