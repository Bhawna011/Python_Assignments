# Assignment - 21 RECURSION Full Stack Web Development using Python MySirG
# 1 Write a recursive python function to print first N natural numbers.
def fun1(n):
    if n>0:
        fun1(n-1)
        print(n)
fun1(15)

# 2. Write a recursive python function to print first N natural numbers in reverse order
def fun2(n):
    if n>0:
        print(n)
        fun2(n-1)        
fun2(10)

# 3 Write a recursive python function to print first N odd natural numbers
def fun3(n):
    if n>0:
        if n%2==0:
            return fun4(n-1)
        else: 
            fun4(n-2) 
            print(n)  
x=int(input("enter a number"))           
fun4(x)  

# 4 Write a recursive python function to print first N odd natural numbers in reverse order
def fun4(n):
    if n>0:
        if n%2==0:
            return fun4(n-1)
        else:
            print(n) 
            fun4(n-2)   
x=int(input("enter a number"))           
fun4(x)  

# 5 Write a recursive python function to print first N even natural numbers.
def fun5(n):
    if n>1:
        if n%2==0:
            fun5(n-2)
            print(n)
        else:
            return fun5(n-1)    
x=int(input("enter a number"))           
fun5(x)  

# 6 Write a recursive python function to print first N even natural numbers in reverse order.
def fun6(n):
    if n>1:
        if n%2==0:
            print(n)
            fun6(n-1)
        else:
            fun6(n-1)    
x=int(input("enter a number"))           
fun6(x)   

#7 Write a recursive python function to print squares of first N natural numbers
def fun7(n):
    if n<1:
        return 1
    fun7(n-1) 
    print(n**2)
x=int(input("enter a number"))           
fun7(x)  

#8  Write a recursive python function to print cubes of first N natural numbers  
def fun8(n):
    if n<1:
        return 1
    fun8(n-1) 
    print(n**3)
x=int(input("enter a number"))           
fun8(x)

# 9 Write a recursive python function to print first N multiples of a given number.
def fun9(n):
    if n<1:
        return 1
    fun9(n-1) 
    print(n*x)
x=int(input("enter a number"))           
fun9(x)

#10. Write a recursive python function to print a number in reverse order.
def fun10(n) :
    if len(n)==0 :
        return n
    return fun10(n[1:]) + n[0]


num =int(input("enter a number"))  
num_str = str(num)

result=fun10(num_str)
print("Reversed Number is: " + result)
