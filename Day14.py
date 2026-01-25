# Sets in Python

# sets-
# is a collection of similar or different type of elements
# syntax-{}
# mutable- we can change
# no duplicate values are allowed i.e it removes duplicated values automatically
# used to store unique values
# used to perform mathimatical operations like union / intersection and differenece
# it doesnt maintain order


sets={"omkar","aditya","nishant","om","snehit","nishant"}
print(type(sets))
print(sets)



# empty tuple
tuple_1=("abc",)
# tuple_2=()
print(type(tuple_1))
print(tuple_1)

# empty sets

# sets_1={"ABC"}
# sets_1={}  #      # X creates a dictionary

sets_1=set()
print(sets_1)
print(type(sets_1))


# union and intersection and differenece

movie_1={"Dhurandhar","Saiyarra","Dhadak 2","Sairat","Marco","Pusha 2","KGF"}
movie_2={"Zindagi Na Milegi Dobara","Misson Impossible","Saiyarra","Tere Ishq Me"}


print(movie_1)
print(movie_2)

# union- it return a unique combination of both the sets
# intersection- it returns a common data from both the sets

# differene- it returns a Items in a A set but not in a B set
   # a.difference(b)


print(movie_1 | movie_2)
# or
print(movie_1.union(movie_2))

# common elements
print(movie_1 & movie_2)
print(movie_1.intersection(movie_2))

# difference
# it returns a items in A but not in a B

print(movie_1-movie_2)
print(movie_1.difference(movie_2))

print(movie_2-movie_1)


###########################################

# pop()- remove

# add()-addd single element 
# update()-add multiple element

emp={"Payal","Alisha","Shrushti","Rutuja","Samruddhi"}
print(emp)
emp.add("Pratiksha")

# multiple data add
emp.update(["Kavya","Isha"])
print(emp)

# pop-Removes random element
emp.pop()
emp.pop()

print(emp)


# remove-remove specfic element
# emp.remove("disha") # error if elements is not found
# emp.discard("disha") # avoid the error if not found
print(emp)

# clear
emp.clear()

print(emp)


no={10,20,30,50,70,200}
print(len(no))
print(max(no))
print(sum(no))
print(sorted(no))

# copy

# frozen set-A frozenset is a set that cannot be changed (like tuples for sets).
# user={"john","doe","mark","sundar","mac"}
user = frozenset(["john","doe","mark","sundar","mac"])
# user.add("andrew")
print(user)