#Assignment - 12 Full Stack Web Development using Python MySirG

          #More on loops

#1. Write a python script to reverse a number.
n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)

#2. Write a python script to check whether a given number is Prime or not.
num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")
#3. Write a python script to print all Prime numbers under 100
lower =2
upper =100

print("Prime numbers under ",upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
#4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)

lower =int(input("Enter a number "))
upper =int(input("Enter a number "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
#5. Write a python script to find next prime number of a given number.

#6. Write a python script to print first N prime numbers
num=int(input("Enter range:"))

print("Prime numbers:",end=' ')

for n in range(1,num):

    for i in range(2,n):

        if(n%i==0):

            break

    else:

        print(n,end=' ')        
#7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
num1= int(input("Please enter the first number: ")) 
num2= int(input("Please enter the second number: ")) 
mn = min(num1, num2) 
for i in range(1, mn+1): 
    if num1%i==0 and num2%i==0: 
     hcf = i 
if hcf == 1: 
 print("Yes! They are Co-Prime.") 
else: 
 print("Sorry! They are not Co-Prime.") 
#8. Write a python script to print first N terms of a Fibonacci series.
num =int(input("Enter a number : "))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
#9. Write a python script to calculate LCM of two numbers.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1
#10. Write a python script to calculate HCF of two numbers.
x = 50
y = 100
if x > y:
  x, y = y, x
for i in range(1,x+1):
  if x%i == 0 and y%i == 0:
    hcf = i

print("HCF of", x, "and", y, "is:", hcf)