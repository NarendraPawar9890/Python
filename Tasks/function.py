# Task 1 – Function to find square of a number
print("Task 1")
def square(n):
    return n * n

print(square(5))

# Task 2 – Function to return maximum of 3 numbers
print("Task 2")
def maximum(a, b, c):
    return max(a, b, c)

print(maximum(10, 25, 15))

#  Task 3 – Function to calculate factorial (using loop)
print("Task 3")
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))

# Task 4 – Function to check even or odd
print("Task 4")
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(7))

# Task 5 – Function to print multiplication table
print("Task 5")
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

table(5)

# Task 6 – Function to count vowels in a string
print("Task 6")
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("Python Programming"))

# Task 7 – Recursive function for countdown
print("Task 7")
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)

# Task 8 – Function with default parameter
print("Task 8")
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Narendra")

# Task 9 – Function returning both sum and average
print("Task 9")
def sum_avg(a, b, c):
    total = a + b + c
    avg = total / 3
    return total, avg

s, a = sum_avg(10, 20, 30)
print("Sum:", s)
print("Average:", a)

# Task 10 – Function using *args to calculate total marks
print("Task 10")
def total_marks(*marks):
    total = 0
    for m in marks:
        total += m
    return total

print("Total Marks:", total_marks(80, 75, 90, 85))