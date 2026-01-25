# Task 1 – Create a dictionary of personal information
Info = {
    "name": "Narendra",
    "age": 21,
    "city": "A.nagara",
    "skills": ["Python", "SQL", "OOP"]
}


# Task 2 – Print all keys and all values separately
print(Info.keys())
print(Info.values())


# Task 3 – Add a new key 'email' and update city
Info["email"] = "narendra@example.com",
Info["city"] = "A.nagar",
print(Info)


# Task 4 – Delete the 'age' key
del Info["age"]
print(Info)


# Task 5 – Create a nested dictionary of two students
students = {
    "student1": {
        "name": "Sahil",
        "age": 23
    },
    "student2": {
        "name": "Rohit",
        "age": 21
    }
}

print(students)


# Task 6 – Check if key 'skills' exists
if "skills" in Info:
    print("skills key exists")
else:
    print("skills key does not exist")


# Task 7 – Use a loop to print all key–value pairs
for key, value in Info.items():
    print(key, ":", value)