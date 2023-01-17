# Assignment - 19  FUNCTION  Full Stack Web Development using Python MySirG
# 1 Write a python program to create a simple function which prints “MySirG” .
def fun1():
     print("MysirG")
fun1()    

# Write a python program to create a function which expects two arguments and print them in the function body.
def fun2(Id,Name):
     print("Id of a student : ",Id)
     print("Name of a student :",Name)

Id=101    
Name="Raam"
fun2(Id,Name)

#Write a python program to create a function which expects an unknown number of arguments.
# Variable length Arguments
def fun3(*t):     #tuple
    Average=sum(t)/ len(t)
    return Average
result=fun3(30,45,60,70,80) 
print("Average is :" , result)   

# 4. Write a python program to create a function which expects kwargs arguments.
def fun4(a,b):
    print("a= ",a , "b=" , b)
fun4(b=3,a=6)   

# 5. Write a python program to create a function which expects a list as an argument.
def fun5(list):
        print(list)
list=["1","Ram" ,"BCA" , "2022"]
fun5(list)

# 6 Write a python program to create a function that finds a maximum of four numbers.
def fun6(num1,num2,num3,num4):
    if (num1>num2) and (num1>num3) and (num1>num4) :
        print ("maximum no is :" , num1)
    elif (num2>num1) and (num2>num3) and (num2>num4):
        print ("maximum no is :" , num2)
    elif (num3>num1) and (num3>num2) and (num3>num4):
         print ("maximum no is :" , num3)
    else:
        print ("maximum no is :" , num4)
fun6(40,45,8,67)    

# 7 Write a python program to sum all the numbers in a list.
def fun7(li):
    sum=0 
    for e in li:
        sum=sum+e
    print("sum",sum)    
li=[3,2,6,4]   
fun7(li)  

# 8 Write a python program to multiply all the numbers in a list.
def fun8(li):
    product=1 
    for e in li:
        product=product*e
    print("product",product)    
li=[3,2,15,4]   
fun8(li) 

# 9. Write a python program to create a function to check whether a number falls in a given range.
def fun9(num):
    if num in range(1,999):
        print(num, "number is in range ")
    else:
        print(num, "number is outside the range ")    
fun9(100)
# 10. Write a python program to create a function to check whether a given number is even or odd.
def fun10(num):
     if num%2==0:
         print( num,"is even number")
     else:
        print( num,"is odd number")   
fun10(67)