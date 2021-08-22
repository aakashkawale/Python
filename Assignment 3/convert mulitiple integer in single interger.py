# Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

a=[11,33,50]
b=""
for i in a:
    c=str(i)
    for j in c:
        b+=j
print(int(b))