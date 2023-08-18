def multiplication():
    
    Num = int(input("Please enter number : "))
    x = int((Num / 10))
    y = Num % 10
    
    if Num >= 10 and Num < 100 : 
        if Num == 00 :
            
         print("GOODBYE")
        
        else :   
            print(x)
            print(y)
            print(x*y)
            multiplication()
    else :
        print("i can't")        # فقط دو رقمی رو میتونه
        
multiplication()        