#Assignment - 5 Operators
#1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
a=int(input("enter a number :"))
output=a//10
print("output is :-" , output)

#2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)
b=int(input("enter a number : "))
answer=b%10
print("answer is :- ", answer)
#3. Write a python script to swap data of two variables.
n=int(input("enter a number :"))
m= int (input("enter a number :"))
temp=n
n=m
m=temp
print("value of n is " , n )
print("value of m is " , m )
#4. Write a python script to find x power y, where values of x and y are given by user.
x=int(input("enter a number : "))
y=int(input("enter a number: "))
z=x**y
print("x power y : " , z)
#5. Write a python script which takes a three digit number from the user and displays only its first digit.
num=int(input("enter a three digit number : "))
first_digit=num//100
print("first digit is : " , first_digit)
#6. Write a python script which takes a three digit number from the user and displays only its middle digit

#7. Write a python script which takes a three digit number from the user and displays only its last digit.
number=int(input("enter a three digit number : "))
Last_digit=number%10
print("last digit is : " , Last_digit)
#8. Write a python script to use IN operator to display the data present in the list.
li=[32,37,17,90,61]
32 in li
#9. Write a python script to use NOT IN operator to display the data not present in list
li=[32,37,17,90,61]
50  not in li
#10. Write a python script to use IS operator to display if both variables are the same object or not? 
a=4
b=4
a is b
a is not b

