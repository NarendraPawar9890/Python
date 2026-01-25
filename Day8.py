# Github 

# print("Welcome {}, year {}".format("Pratik", 2025))

# a=34
# b=a
# c=55
# print(b)
# print(id(b))

# b=c

# print(b)
# print(id(b))

# a=1
# b=10
# print(a%b)

for i in range(1, 6):
    print(i)


for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

for i in range(10, 0, -1):
    print(i)

for i in range(1, 6):
    print("*" * i)

for i in range(5, 0, -1):
    print("*" * i)

def info(**data):
    for key, value in data.items():
        print(key, ":", value)

info(name="Ravi", age=22, city="Pune", g=298)

def factorial(n):
    if n == 0:
        return 1   # Base Case
    else:
        return n * factorial(n - 1)   # Recursive Case

print(factorial(10))

def total(n):
    if n == 1:
        return 1
    return n + total(n - 1)

print(total(10))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # 6