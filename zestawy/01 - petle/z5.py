target = int(input("S = "))

# Summing
a1 = 1
b1 = 1

# Removing
a2 = 1
b2 = 1
total = 0

# 1 1 2 3 5 8 13 21

while total < target:
    total += a1
    next = a1 + b1
    a1 = b1
    b1 = next

while total > target:
    total -= a2
    next = a2 + b2
    a2 = b2
    b2 = next

if total == target:
    print("YES")
    exit(0)

print("NO")