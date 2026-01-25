# Python list

# lists- is a collection of similar of different data type of elements
# stored in. []
# starts indexing from 0
# we can stored mulitple type of data in a single variable
# Mutable- we can change, add,remove, or update


# int - a=20
# string- a="" or ''
# boolean- True | False
# None-  empRole=None
# float- a=23.5

###################################################
# NPDT

list=[10,325.3,True,None,"Narendra"]
print(list)
skills=["HTML","JS","React JS","Node JS","Express JS","CSS","Tailwind","Next JS","MongoDB","PostregsSQL"]
print(skills)




# access list elements- indexing

print(skills[0])
print(skills[1])

#(negative index = from end)
print(skills[-1]) # PostgresSQL
# print(skills[10]) # error  list index out of range


# to check length of a s list
print(len(skills))

#######################################################

# we can update given lists

roles=["admin","manager","user"]

# update list element
roles[2]="super-admin"

print(roles)

# adding elements to the end of list
# append()
roles.append("HR")
print(roles)



######################################################


# add element on specific index
# insert(index,value)

roles.insert(0,"HR")
roles.insert(1,"HR")
print(roles)



#############################################################

# extend- used to merge or concatenate 2 or more lists
# modifed original list

list_1=["100","200",500,"OM","Vaibhav","Aditya"]
list_2=[True,None,"ABC","XYZ"]

# without extend
# for x in list_2:
#     list_1.append(x)

# 2
# print(list_1+list_2)

# 3
# print(list_1,list_2)


# with extend

list_1.extend(list_2)

print(list_1)

###########################################

# pop()- used to remove elements from lists

# pop()- by default it will remove last element
# pop(index)- Now it will remove specific element

list_3=[10,20,30,40,50,60,70]
list_3.pop()
list_3.pop()
list_3.pop(2) 
print(list_3)

#############################################

# reverse 
list_3.reverse()

print(list_3)

# sort()
# it sorts the list elements alphabetically or numerically

fruits = ["apple",  "cherry","pomegrante","grapes","orange","banana","pineapple","custard apple","watermelon"]
fruits.sort()
print(fruits)

no=[100,300,500,250,350,50,30,1000,100]
no.sort()
no.reverse()
print(no)

###########################################

# clear- empty lists

list_4=[10,40,50,80]
list_4=[]

# or

# list_4.clear()

print(list_4)


# remove()
# remove 1st matching element

list_5=["HTML","CSS","Next JS","Redux","MUI","CSS"] 
list_5.remove("CSS")
print(list_5)


#############################################################

# copy- most IMP

# user=["Pratik","Bhavesh","Shubham","Aniket","Aditya"]
# roles=["MERN Stack","Python Dev","AI Engineer","SDE-1","L-1"]

# assign roles in a new_roles variable
# new_roles=roles
# new_roles.append("Senior Product manager")

# print(roles)
# print(new_roles)

# **********************

# problem

# it has changes both the lists
# to avoid this make a independent copy of new list so it will not affect on original list


# solution-copy()
# create independent copy


roles=["MERN Stack","Python Dev","AI Engineer","SDE-1","L-1"]

# shallow copy
new_roles=roles.copy()
new_roles.append("Vice President")

print(roles)
print(new_roles)


# 🔍Searching in a List

emp=["Narendra","Sanmesh","Aditya","Om","Snehit","Narendra"]

# membership operator- in and not in

print("Narendra" in emp)
print("ABC" in emp)
print("ABC" not in emp)

# ***********************

# looping

for x in emp:
    print(x)

# count
print(emp.count("Pratik"))


# built in function
# len()
# min()
# max()-
# sum()

list_6=[10,40,50,80,90,300,30]
print(max(list_6)) # 300
print(min(list_6))
print(sum(list_6))
print(len(list_6))


# Slicing- extract some part of a list
# small piece of data

# syntax-[start:end] ignore last
print(list_6[1:3]) # 40,50

print(list_6[0:5]) # 10 ...90
print(list_6[2]) # 50
print(list_6[2:]) # 50......
print(list_6[:3])
print(list_6[:])


##########################################################
# Practice
# 1️⃣ Create a list of 5 subjects and print them one by one.
# 2️⃣ Add a new subject in the middle using insert().
# 3️⃣ Remove one subject using remove().
# 4️⃣ Sort the list alphabetically.
# 5️⃣ Create a new list [1,2,3,4,5] and print their squares using list comprehension.
# 6️⃣ Create a nested list of students and print the 2nd student’s name.


subject=["Python","DSA","DBMS","CN","DT"]
for i in subject:
    print("Subject:",i)

subject.insert(3,"DM")

subject.remove("CN")

subject.sort()

for i in subject:
    print("Sorted Subject:",i)

squares = [i*i for i in range(5)]
print(squares)


Std=[["abc","20"],["xyz",21]]
print(Std[1][0])