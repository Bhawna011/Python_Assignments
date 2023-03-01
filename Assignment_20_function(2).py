# Assignment - 20 Full Stack Web Development using Python MySirG

                  #More on functions

# 1. Write a python program to create a function that takes a list and returns a new list
# with the original list's unique elements.
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 
# 2. Write a python program to create a function that takes a number as a parameter and
# checks if the number is prime or not.
def check_prime(n):
	    if (n==1):
	        return False
	    elif (n==2):
	        return True
	    else:
	        for x in range(2,n):
	            if(n % x==0):
	                return False
	        return True             
print(check_prime(11))

# 3. Write a python program to create a function that prints the even numbers from a
# given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even(l):
    l2=[]
    for i in l:
       if i%2==0:
           l2.append(i)

    return l2
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result=even(l)
print(result)

# 4. Write a python program to create a function that checks whether a passed string is palindrome or not.
def strPalindrome(s,start,end):
    while start<=end:
        if s[start]==s[end]:
            start=start+1
            end=end-1
        else:
            return False
    return True         
s="nitin"
#s="abcddcba"
#s="mango"
start=0
end=len(s)-1
result=strPalindrome(s,0,end)
print (result)

# 5. Write a python program to create a function to find the Min of three numbers.
def minimum(a, b, c):
 
    if (a <= b) and (a <= c):
        smallest = a
 
    elif (b <= a) and (b <= c):
        smallest = b
    else:
        smallest = c
         
    return smallest
 
a = 10
b = 14
c = 12
print(minimum(a, b, c))

# 6. Write a python program to create a function and print a list where the values are
# square of numbers between 1 and 30.
def fun():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l)
		
fun()
#7. Write a python program to access a function inside a function.
def num1(x):
   def num2(y):
      return x * y
   return num2
res = num1(10)

print(res(5))

# 8. Write a python program to create a function that accepts a string and calculate the
# number of upper case letters and lower case letters.
x=input("Enter the string:- ")
def char(x):
  u=0
  l=0
  for i in x:
      if i>='a' and i<='z':
       l+=1

      if i >='A' and i<='Z':
       u+=1

  print("LowerCase letter in the String",l)
  print("UpperCase letter in the String",u)
char(x)

# 9. Write a python program to create a function to check whether a string is a pangram or not.
# from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
strng=input("Enter string:")
if(check(strng)==True):
      print("The string is a pangram")
else:
      print("The string isn't a pangram")

# 10. Write a python program to create a function to check whether a string is an anagram or not.
def check(s1, s2):
     
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
s1 ="listen"
s2 ="silent"
check(s1, s2)