# Assignment - 11 Full Stack Web Development using Python MySirG
         # loops
#1. Write a python script to calculate sum of first N natural numbers.
n=int(input("enter a number :"))
sum = 0
while(n > 0):
    sum=sum+n
    n=n-1
print("The sum of first n natural numbers is",sum)

#2. Write a python script to calculate sum of squares of first N natural numbers
n=int(input("enter a number :"))
sum = 0
for i in range(1, n+1):
    sum += (i*i)

print("Sum of squares = ", sum)
#3. Write a python script to calculate sum of cubes of first N natural numbers
n=int(input("enter a number :"))
sum = 0
for i in range(1, n+1):
    sum += (i*i*i)

print("Sum of squares = ", sum)
#4. Write a python script to calculate sum of first N odd natural numbers.
n=int(input("Enter a number :"))
sum=0
for i in range(1,n+1,2):
    sum= sum+i
    print(sum , end ="\n")
#5. Write a python script to calculate sum of first N even natural numbers
n=int(input("Enter a number :"))
sum=0
for i in range(2,n+1,2):
    sum= sum+i
    print(sum , end ="\n")
#6. Write a python script to calculate factorial of a given number.
num=int(input("enter a number :"))
fact=1
for i in range(1,num + 1):
       fact = fact*i
print("The factorial of",num,"is",fact)
#7. Write a python script to count digits in a given number.
n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)
#8. Write a python script to calculate sum of digits of a given number
n=int(input("Enter a number:"))
sum=0
while(n>0):
    digits=n%10
    sum=sum+digits
    n=n//10
print("The total sum of digits is:",sum)
#9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method).
n=int(input("Enter a number: "))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i,end=" ")
#10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
decimal = int(input("Enter a decimal number: "))
octal = 0
ctr = 0
temp = decimal  
 
while(temp > 0):
    octal += ((temp%8)*(10**ctr)) 
    temp = int(temp/8)             
    ctr += 1
       
print("Binary of {x} is: {y}".format(x=decimal,y=octal))