#Assignment - 18 Full Stack Web Development using Python MySirG

                 #Dictionary

#1. Write a python program to create and print a dictionary which stores your information.
(name, age, gender .....)
d1={"name":"Priya","age": 24,"gender":"Female" }
print(d1)

#2. Write a python program to access the items of a dictionary by referring to its key name.
d2 = {
  "name": "Riya",
  "gender": "Female",
  "age": 24
}
x = d2["name"]
print(x)

#3. Write a python program to get a list of the values from a dictionary.
d3={
    "a":10 , "b":12 ,"c":21 , "d":32 , "e":33
    }

print(d3.values())

#4. Write a python program to change the value of a specific item by referring to its key name.
d4 = {
    "name": "Riya",
    "gender": "Female",
   "age": 24
}
d4["age"]=25
print(d4)

#5. Write a python program to print all key names in the dictionary, one by one.
d5={
     "a":10 , "b":12 ,"c":21 , "d":32 , "e":33
    }
for k in d5:
    print(k)

#6. Write a python program to create a dictionary that contains three dictionaries.(nested)
students = {
  "section_A" : {
    "name" : "Raj",
    "stream" :"Science"
  },
  "section_B" : {
    "name" : "Raja",
    "stream" :"commerce"
  },
  "Section_C" : {
    "name" : "Rani",
    "stream" :"Humanities"
  }
}

print(students)

#7. Write a python program to create three dictionaries, then create one dictionary that
#will contain the other three dictionaries.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)

#8. Write a python program to convert two lists into a dictionary in a way that item from
#list1 is the key and item from list2 is the value.
l1=(1,2,3,4)
l2=("A","B","C","D")
d8 = dict(zip(l1,l2))
print(d8)

#9. Write a python program to merge two python dictionaries into one dictionary.
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print({**dict_1, **dict_2})

#10. Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
 'C': 92,
 'Java': 66,
 'Python': 85
 }
d10 = {key:val for key,val in sample_dict.items() if val == min(sample_dict.values())}
print(d10)