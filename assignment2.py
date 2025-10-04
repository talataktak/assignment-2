attempts = 0

while attempts < 3 :
   username = input ("Enter your username: ")
   password = input ("Enter your password: ")
   if username == "admin" and password == "1234":
     print ("Login Successful! ")
     
     N =  int ( input ("Enter a number N : "))
     for d in range (2 , N +1 ) :
        is_prime = True;
        for i in range (2,d) :
            if d % i == 0 :
                is_prime = False
            break;
    
        if is_prime :
         print ( d , end=" ")

     print ()
     break 
   else :
       attempts += 1
       if attempts == 3 :
         print ("Account Locked ! ")
         exit ()

    



