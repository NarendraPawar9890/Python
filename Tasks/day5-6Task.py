# Task 1 – Print numbers 1 to 10 using a for loop
for i in range(1, 11):
    print(i)
##################################################################################################

# Task 2 – Print even numbers 1 to 20
for i in range(1,21):
    if i%2==0:
        print("Even No in 1 to 20:",i)

##################################################################################################

# Task 3 – Positive, negative, or zero check
n = int(input("Enter No..."))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

##################################################################################################

# Task 4 – Print your name 5 times
for _ in range(5):
    print("Narendra")
    
##################################################################################################

# Task 5 – Sum of numbers 1 to 100
print(sum(range(1, 101)))

##################################################################################################

# Task 6 – Multiplication table of a number
n = int(input("Enter No..."))
for i in range(1, 11):print(n * i)
    
##################################################################################################

# Task 7 – Check if divisible by 5 and 11
n = int(input("Enter No to check divisibile by 5 and 11..."))
if n % 5 == 0 and n % 11 == 0:
    print("Divisible")
else:
    print("Not Divisible")
    
##################################################################################################

# Task 8 – Reverse numbers 10 → 1
for i in range(10, 0, -1):
    print(i)
    
##################################################################################################

# Task 9 – Find largest of 3 numbers
print("Check Largest No....")
a = int(input("Enter no1..."))
b = int(input("Enter no2..."))
c = int(input("Enter no3..."))
print("Largest NO is:",max(a, b, c))

##################################################################################################

# Task 10 – Password validation loop until "python123"
while True:
    p = input("Enter a password:")
    if p == "python123":
        print("Access Granted")
        break

##################################################################################################

# Task 11 – Fibonacci series
n = int(input("Enter Fibonacci no.."))
a,b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b
    
##################################################################################################

# Task 12 – Prime number check
n = int(input("Enter no to cehck a prime or not..."))
if n > 1 and all(n % i != 0 for i in range(2, n)):
    print("Prime")
else:
    print("Not Prime")
    
##################################################################################################

# Task 13 – Menu-driven calculator using match-case
print("Calculator...")
a = int(input("Enter 1st no..."))
b = int(input("Enter 2nd no..."))
op = input("Enter operation +,-,*,/...:")

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)