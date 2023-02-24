# Assignment - 30 Full Stack Web Development using Python MySirG for loop and range

# 1. Write a python script to print the first 10 multiples of 5.
for i in range (1,11):
    print( "The multiple of 5 = ", 5*i , end="\n")

# 2. Write a python script to print first 10 multiples of N
n=int(input("Enter a number :"))
for i in range (1,11):
    print( "The multiple  = ", n*i , end="\n")

# 3. Write a python script to print first M multiples of N.
n=int(input("Enter a number :"))
m=int(input("Enter a number :"))
for i in range (1,m+1):
    print( "The multiple  = ", n*i , end="\n")

# 4. Write a python script to print the first 10 multiples of N in reverse order.
n=int(input("Enter a number :"))
for i in range (10,0,-1):
    print( "The multiple  = ", n*i , end="\n")

# 5. Write a python script to print table of user’s choice.
n=int(input("Enter a number : "))
for i in range (1,11):
    print(n,"x",i,"=",n*i)

# 6. Write a python script to print first N even natural numbers.
n=int(input("Enter a number :"))
even=2
for i in range(n):
    print(even , end ="\n")
    even=even+2

# 7. Write a python script to print first N odd natural numbers
n=int(input("Enter a number :"))
odd=1
for i in range(n):
    print(odd , end ="\n")
    odd=odd+2

# 8. Write a python script to print squares of first N natural numbers.
n=int(input("Enter a number :"))
for i in range (1,n+1):
    print(i*i , end="\n")
    
# 9. Write a python script to print cubes of first N natural numbers.
n=int(input("Enter a number :"))
for i in range (1,n+1):
    print(i*i*i , end="\n")

# 10. Write a python script to display all prime numbers within a range.
# range start = 15 end = 45
start=15
end=45
print ("The Prime Numbers in the range are: ")  
for number in range (start, end + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)    