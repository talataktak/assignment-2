def sum_score_recursive (scores): 
    if len(scores) == 0:                      
        return 0 
    else:                                    
        return scores[0] + sum_score_recursive (scores[1:])
    

def students () :
    number = int (input ("Enter Number of Students : "))
    names = []
    scores = []


    for i in range (int ( number )) :
       name = input ( "Enter student " + str ( i+1 ) + " name : ")
       score = float (input ( "Enter " + name + "'s score : "))
       names.append (name)
       scores.append (score)

     
    print ( "All Students and Scores : ")
    for i in range (int ( number )) :
       print ( names [i] +" - " + str (int (scores [i])))


    total = sum_score_recursive(scores)
    avg = total / len(scores)
    print("Average Score:", avg)


    d = scores[0]
    top_name = names[0]
    for i in range (int ( number )) :
         if d < scores[i] :
            d = scores[i]
            top_name = names[i]
    print ( "Top Student : " + top_name + " ( " + str ( int (d ) )+ " ) ") 

    for i in range (int ( number )) :
        if scores [i] < 60 :
            print ("Failed Students : " + names[i] )
             

students ()



 

    


    
