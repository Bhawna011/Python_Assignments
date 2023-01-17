# Assignment - 9 Full Stack Web Development using Python MySirG While Loop
# 1. Write a python script to print MySirG N times on the screen
n=int(input("Enter a number :"))
i=1
while i<=n:
    print("MySirG")
    i=i+1

#2. Write a python script to print first N natural numbers
n=int(input("Enter a number :"))
i=1
while i<=n:
    print(i)
    i=i+1

#3. Write a python script to print first N natural numbers in reverse order
n=int(input("Enter a number :"))
i=1
while n>=i:
    print(n)
    n=n-1

#4. Write a python script to print first N odd natural numbers          
x=int(input("Enter a number"))  
i=1
n=x
while n>i:
    if n%2==0:
        n=n-1
    else:
        print(i)
        i=i+2  
print(n)         

#5. Write a python script to print first N odd natural numbers in reverse order  
x=int(input("Enter a number"))  
i=1
n=x
while n>i:
    if n%2==0:
        n=n-1
    else:
        print(n)
        n=n-2  
print(n)

#6. Write a python script to print first N even natural numbers.                 
x=int(input("Enter a number"))  
i=1
n=x
while n>i:
    if n%2==0:
        print(i+1)
        i=i+2     
    else:
        n=n-1        
print(n)         


#7. Write a python script to print first N even natural numbers in reverse order. 
x=int(input("Enter a number"))  
i=1
n=x
while n>i:
    if n%2==0:
        print(i+1)
        i=i+2     
    else:
        n=n-1        
print(n)         

#8. Write a python script to print squares of first N natural numbers
x=int(input("Enter a number :"))
i=1
n=x
while i<=n:
    print(i*2)
    i=i+1  
#9. Write a python script to print cubes of first N natural numbers.
x=int(input("Enter a number :"))
i=1
n=x
while i<=n:
    print(i**3)
    i=i+1    
        
# 10. Write a python script to print first 10 multiples of N.
x=int(input("Enter a number :"))
i=1
n=x
while i<=n:
    print(i*x)
    i=i+1   
