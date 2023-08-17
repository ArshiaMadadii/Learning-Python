#عدد تام
def Perfect_Number() :
        Entrance = int(input("Please enter number : "))     #ورودی عدد را میگیرد و اینتجر میکند
        sum = 0
        for Perfect_number in range (1,(Entrance - 1)):      # از یک تا یک عدد قبل از عدد مدنظر را پیدا میکند
            if Entrance%Perfect_number == 0:                  # دنبال سری اعدادی میگردد که بر عدد انتخاب شده بخش پذیر باشد
                sum += Perfect_number                     # هر بار عدد را با صفر و اعداد قبلی بخش پذیر جمع میکند
        if sum == Entrance :                              
            print('Perfect number')
        else:
            print("Not perfect number")                
        new_game = input("Do you like to continue this game?")
        if new_game == 'Yes':
            Perfect_Number()
        else:
           print('bye bye')    
     
         
Perfect_Number()