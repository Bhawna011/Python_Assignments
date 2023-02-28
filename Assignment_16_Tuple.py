#Assignment - 16 Full Stack Web Development using Python MySirG

                      #Tuple

#1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using tuple
t1=("Java" , "Python", "SQL", "C")
print(t1)
#2. Write a python program to store only one item using tuple.
t2=(10,)
print(t2)
#3. Write a python program to reverse the tuple.
t3 = (1, 2, 3.78, 9.56,"Python")
t3 = tuple(reversed(t3))
print(t3)
#4. Write a python program to Swap two tuples in Python.
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)
#5. Write a python program to check if all items in the tuple are the same.
thistuple = ("C", "JavaScript", "Python")
if "C" in thistuple:
  print("Yes, 'C' is in the fruits tuple")

#6. Write a python program to divide the tuple into four variables.
tuple1=(100, 200, 300, 400)

print("initial list", str(tuple1))
 
res = tuple(zip(*[iter(tuple1)]*1))
 
print("resultant tuples", str(res))
#7. Write a python program to copy elements 4 and 5 from the following tuple into a new  tuple.
tuple1=(1,2,3,4,5,6)
tuple2=tuple1[3:5]
print(tuple2)

#8. Write a python program to Sort a tuple of tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)
#9. Write a python program to print the value 20 from given nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

print(tuple1[1][1])
#10. Write a python program to change the first item (22) of a list within the following tuple to 222.
#tuple1 = (11, [22, 33], 44, 55)
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)