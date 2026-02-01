# dictionaries


age=20
is_eligible=True
address="Pune"
ctc=20.5
empRole=None

skill=["React","Node JS","Express","Next JS"]

# dict / object

# emp={
#     # key:value
#     "name":"Pratik",
#     "skill":{
#         "skill1":"React",
#         "skill2":"Node JS"
#     }

# }

# used to stored large amount of data in a key value pair
# having methods and properties
# redable data

# mutable
# access data via named indexing



emp={

    "id":1,
    "name":"Pratik",
    "skill":["Python","AI","Devops"],
    "CTC":'10LPA',
    'role':"Python Developer",
    "company":"Accenture",
    "onRole":True,
    "age":21.5,
    "promotion":None,
    "age":20,
}
print(emp)


# access

print(emp["role"])
print(emp["skill"])


print(emp["skill"][1])

print(emp["company"])


# no duplicate keys are allowed if duplicat keys are there then it will consider last one
print(emp["age"])


# update

emp["role"]="AI Engineer"

print(emp)

print(emp["role"])


# add new keys
emp["email"]="pratik.works@gmail.com"
print(emp)


#################################################

# looping


# for in


# it will return keys 
# for x in emp:
#     print(x)

# methods


# keys
for keys in emp.keys():
    print(keys)

# values
# it returns a values from dict
for x in emp.values():
    print(x)



# items
# it returns a both key and value pair
for x in emp.items():
    print(x)


#################################3333

# membership operator- in and not in

# check exists or not
res="role" in emp
print(res)

res="role" not in emp
print(res)


# len
# copy
# clear
# type

print(len(emp))
print(type(emp))
emp.clear()


print(emp)

# copy
# it creates a shallow copy / independent copy of a existing dict


dict1={
    "user":"Omkar",
    "email":"omkar@gmail.com"
}


dict2={
    "address":"Pune",
    "skill":"Python"
}

# dict3=dict2

# dict2["skill"]="AI Engineer"
# dict2["role"]="Software Developer"

# copy
dict3=dict2.copy()
dict2["skill"]="AI Engineer"


print(dict1)
print(dict2)
print(dict3)


# update- Updates one dictionary with another

products={
    "productName":"Mac",
    "productPrice":"1lac",
    "productDetails":{
        "ram":"16GB",
        "rom":"256 GB",
        "processor":"m4"
    }
}
products.update({"productOfferPrice":"80000","productBrand":"Apple"})
# print(products)

# pop
# used to remove data

# must passed key name
products.pop("productDetails")

print(products)

# list=>tuple
list3=["mahesh","Sanket","Om","Aditya"]
print(list3)
print(tuple(list3))

# dict
# list of tuples
list4=[("age","address"),(23,"Nagar")]
print(list4)
print(dict(list4))


# setDefault=used to set default values 
# if key is present then it will consider existing  one else default one

student={
    "name":"Om",
    "address":"Nagar",
    # "role":"MERN Stack Developer"
}

student.setdefault("role","Software Trainee")


print(student)

