import random
def Game():
 print('Whats your name?')
 name = input()
 print('Hi', name ,'are you ready?')
 age = int(input('How old are you?'))
 if age <= 3:
     print('You are very small')
     Game()
 else :        
    answer = input('do u like this game')
    if answer == "no":
        print('bye bye', name)
        Game()
    
        
    elif answer == 'Yes':
        print('Start Game')
    a = 1
    b = 99
    bazi  = True
    while bazi :
        Hads = random.randint( a , b )
        print("Javab", Hads ,"mishe?")
        Javab = input("'BozorgTar','KochikTar','Khodeshe'")
        
        if Javab == 'BozorgTar':
            a = Hads
            Hads = random.randint(a,b)
            
        elif Javab == 'KochikTar':
            b = Hads
            Hads = random.randint(a,b)
            
        elif Javab == 'Khodeshe' :
            bazi  != False
            print('Hal kardi?', Hads , 'bedastOmad') 
            break
            
        #else :
            # print("Javab", Hads ,"mishe?")
            #Javab = input("'BozorgTar','KochikTar','Khodeshe'")    
            
    new_game = input("Do you like to continue this game?")
    if new_game == 'Yes':
        Game()
    else:
        print('bye bye', name)    
    
         
Game()           
             
         
