
# Task 1 – Create a list of 5 subjects and print them one by one


subject=["Python","DSA","DBMS","CN","DT"]
for i in subject:
    print("Subject:",i)

# Task 2 – Add a new subject in the middle using insert()
subject.insert(3,"DM")
print(subject)

# Task 3 – Remove one subject using remove()
subject.remove("CN")

# Task 4 – Sort the list alphabetically
subject.sort()
print("Sorted Subject:",subject)

# Task 5 – Create a list [1,2,3,4,5] and print their squares using list comprehension
# ex1-
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)

# ex2-
squares = [i*i for i in range(5)]
print(squares)

# Task 6 – Create a nested list of students and print the 2nd student’s name
Std=[["abc","20"],["xyz",21]]
print(Std[1][0])
