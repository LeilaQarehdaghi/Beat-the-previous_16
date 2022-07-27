import math


while True:
    num =input(' Enetr your number: ')
    
   #checking the num is negative or not
    if not num.isnumeric():
        print('please enter an integer number')
    elif int(num)<0:
       print('please enter a posetive number')
    else: 
        break


left_string=[]
list1= []
count=[]
lennum = len(num)
len_left_string = len(left_string)

list1.append(num[0])
flag = 0
x=''

for i in range(1,lennum+1):
    if i in count:
        pass
    else:
        if num[i] > list1[-1]:
            list1.append(num[i])
            left_string.append(num[i+1:])
            count.append(i)
            print(list1)
            print(count)
            print(left_string)

        else:
            while x > list1[-1]:
       

                    x =i  +(i+1)
     
                       

                        
               
                      
              

print(count)
print(left_string)

print(list1)

                          
                
                
        
        
        
            

    

    
   
        




    
    

                                           
    
    
      
    

    

    





    
        
