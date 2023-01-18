# Assignment - 15   Strings Full Stack Web Development using Python MySirG

# 1. Write a python script to create a String in 3 different possible ways.
s1="Python"
s2=str(123)
s3="""Javascript"""
print(s1,s2,s3)

# 2. Write a python script to Get the characters from the start to position 5 (Given String
# “iNeuron” using the slice syntax)
s="iNeuron"
print(s[:5])

# 3. Write a python script to Get the characters from position 2 to position 5 (Given String
# “Hello Learners” using the slice syntax)
h="Hello Learners"
print(h[2:5])

# 4. Write a python script to demonstrate String Concatenation adding space in between (Given Strings a=”Learning” b=”Python” )
a="Learning"
b="Python"
c = a + " " + b
print(c)

# 5. Write a python script to get the count of total number of characters in String a=“iNeuron”
a="iNeuron"
print(len(a))

# 6. Write a python script to reverse a String. (“iNeuron”)
r="iNeuron"
print(s[::-1])

# 7. Write a python script to determine whether a string contains a specific substring.
string="Full Stack Web Development using Python MySirG"
substring="MySirG"
print(["yes" if substring in string else "no"])

# 8. Write a python script to check if a string contains only numbers.
string1="1234"
print(string1.isdigit())
string2="abcs12"
print(string2.isdigit())

# 9. Write a python script to check if a string contains only characters of the alphabet.
s3="1234"
print(s3.isalpha())
s4="abcd"
print(s4.isalpha())
s5="abcd123"
print(s5.isalpha())

# 10. Write a python script to convert an integer to a string.
n=(int(input("enter some numbers")))
print(type(n))
s=str(n)
print(type(s))