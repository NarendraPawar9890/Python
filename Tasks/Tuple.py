# # list vs tuple

# Feature             List                                                Tuple
# Syntax          my_list = [1, 2, 3] (Square brackets)       my_tuple = (1, 2, 3) (Parentheses)
# Mutability      Mutable (Can be changed)                    Immutable (Cannot be changed)
# Size            Larger memory overhead                      Smallermemory overhead
# Performance     Slower (due to extra functionality)         Faster (more efficient for the CPU)
# Methods         Many (append, remove, pop, sort, etc.)      Few (only count and index)


# 4️⃣ Count how many times `"apple"` appears in `("apple", "banana", "apple")`.
fruits=("apple", "banana", "apple")
print(fruits.count("apple"))


# 5️⃣ Unpack a tuple `(10, 20, 30)` into 3 variables.

tuple1=(10,20,30)
no1,no2,no3=tuple1
print(no1)
print(no2)
print(no3)

# 6️⃣ Create a nested tuple and access the second row, third element.

tuple2=((1,2,3,4,),(5,6,7,8,9))
print(tuple2[1][2])

# 1️⃣ Create a tuple of 5 colors and print them one by one.
colors=("red","blue","yrllow","green","black")
for i in colors:
    print("Colors:",i)
