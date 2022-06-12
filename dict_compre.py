def run():
    my_dict= {}

    for i in range(1,101):
         if i%3 !=0:
            
             my_dict[i]= i**3
    
    
    my_dict2 = {i:i**3 for i in range(1,101) if i%3 !=0}
    
        
    
    if my_dict==my_dict2:
        print("Both dictionaries are equal in fact: "+ str(my_dict[1])+"="+str(my_dict2[1]) )
    else:
        print("The dicctionaries are differents")
        
    
    

if __name__ == '__main__':
    run()