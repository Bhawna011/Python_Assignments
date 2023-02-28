#Assignment - 17 Full Stack Web Development using Python MySirG

                            #Set

#1. Write a python program to store all the programming languages known to you using Set.
s1={"C","JavaScript","Python"}
print(s1)
#2. Write a python program to store your own information {name, age, gender, so on..}
myset={"Priya",25,Female,"BCA"}
print(myset)
#3. Write a python script to get the data type of a Set.
s3={2,3,4}
print(type(s3))
#4. Write a Python script to find if “Python” is present in the set thisset = {"Java","Python", "Django"}
thisset = {"Java","Python", "Django"}
if "Python" in thisset:
    print("yes , Python is present")
#5. Write a python program to add items from another set to the current set. thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
thisset.update(secondset)
print(thisset)
#6. Write a python program to add elements of list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset.update(mylist)
print(thisset)
#7. Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", “SQL”}
thisset = {"Python", "Django", "JavaScript","SQL"}
thisset.pop()
print(thisset)
#8. Write a python program to delete the set completely.
names = {'Priya', 'Meera', 'Riya'}
print("(before clear):", names)
names.clear()
print('(after clear):', names)
#9. Write a python program to loop through the set and print values
thisset = {"Python", "Django", "JavaScript", “SQL”}
thisset = {"Python", "Django", "JavaScript","SQL"}
for e in thisset:
    print(e)
#10. Write a python program to find the maximum and minimum value in a set.
set = {5, 10, 3, 15, 2, 20}
print("Original set elements:")
print(set)
print(type(set))
print("\nMaximum value of the set:")
print(max(set))
print("\nMinimum value of the set:")
print(min(set))