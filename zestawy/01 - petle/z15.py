def sp(n) -> int:
    sum = 1
    i = 2
    while i*i < n:
        if n % i == 0:
            sum += i + n//i
        i += 1
    if i*i == n:
        sum += i
    return sum

for a in range(1, int(1e6)):
    b = sp(a)
    if b < a and sp(b) == a:
        print(a, b)