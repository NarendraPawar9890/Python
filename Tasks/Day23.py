# 1️⃣ String Logic

# Q: Reverse a string without using reverse function
# 👉 What to observe: loop logic, indexing

string = "narendra"
reverse = ""

for i in range(len(string) - 1, -1, -1):
    reverse = reverse + string[i]

print("Reversed string:",reverse)


# 2️⃣ Number Logic

# Q: Check whether a number is palindrome
# Example: 121 → Yes, 123 → No 

no1=121
temp=str(no1)
pal=""

for i in range(len(temp)-1,-1,-1):
    pal=pal+temp[i]

if no1==int(pal):
    print("palindrome")

else:
    print("Not Palindrome")


# 3️⃣ Counting Logic

# Q: Count vowels in a string
# Extra follow-up: Ignore case? 

text = "jdhfjhkawekifo"
count = 0

for i in text.lower():
    if i in "aeiou":
        count += 1

print("Vowels count :", count)

# 4️⃣ List Logic

# Q: Find duplicate elements in a list
# Follow-up: Without using set()

elements = [1, 2, 3, 2, 4, 5, 1, 6 , 7, 8, 7, 5]
duplicates = []

for i in range(len(elements)):
    for j in range(i + 1, len(elements)):
        if elements[i] == elements[j]:
            if elements[i] not in duplicates:
                duplicates.append(elements[i])

print("Duplicate elements:", duplicates)
