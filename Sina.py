for Number in range(10000,99999):
    
     if int(str(Number)[0])==2*int(str(Number)[1])-1:
        
        if int(str(Number)[4])+int(str(Number)[2]) == 14:
          
           if int(str(Number)[3])==int(str(Number)[1])+1:
              
              if int(str(Number)[1])+int(str(Number)[2]) == 10:
                 
                 if int(str(Number)[0])+int(str(Number)[1])+int(str(Number)[2])+int(str(Number)[3])+int(str(Number)[4])==30:
                    print(Number)