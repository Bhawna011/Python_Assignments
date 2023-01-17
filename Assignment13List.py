#Assignment - 13  List Full Stack Web Development using Python MySirG

# 1. Write a python script to store multiple items in a single variable ( Items are “Java” ,“Python”, “SQL”, “C” ) using list
li=["Java","Python","SQL","C"]
print(li)

# 2. Write a python script to get the data type of a list.
mylist = ["Python", "C++", "jAVASCRIPY"]
print(type(mylist))

# 3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
mylist = ["Java", "C", "Python"]
print(mylist)
print(mylist.pop())

# 4. Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
print(thislist)
thislist[1]="NoSQL"
thislist[3]="Flutter"
print(thislist)

# 5. Write a python script to add an item to the end of the list (item “Python”. (mylist =["Java", "SQL", "C", "Reactnative"]
mylist =["Java", "SQL", "C", "Reactnative"]
print(mylist)
mylist.append("Pyhton")
print(mylist)

# 6. Write a python program to append elements from another list to the current list.(
# firstlist = ["Java", "Python", "SQL"]
# secondlist = ["C", "Cpp", "NoSQL"] )
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
print(firstlist) 
firstlist.append(secondlist)
print(firstlist)

# 7. Write a python program to Print all items by referring to their index number (thislist =
# ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for e in thislist:
    print (e,end=',')
    
# 8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
# "C", "Reactjs", "Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
print(thislist)
thislist.sort()
print(thislist)

# 9. Write a Python script to create a list of city names taken from the user.

# 10. Write a Python script to create a list, where each element of the list is a digit of a given number.
li=[x for x in input("enter number: ")]
print(li)