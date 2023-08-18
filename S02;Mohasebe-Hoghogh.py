def Salam(name):
    print( 'salam' , name ,'Hoghogh in mahet ro hesab kardam' , ':')
    
def Daramad(S , P):
    Hoghog = S * P
    if S < 5: 
        return ' BishTar Talash Kon ' 

    elif Hoghog > 20 :
         Hoghog = Hoghog * 1.2
        
    else :
        Hoghog = S * P        

    return Hoghog

def bye(name):
    print('Moafagh Bashi' , name)
    
name = input()
S = int(input()) 
P = int(input()) 

Salam(name)
print (Daramad( S , P ) , '$')
bye(name)
        