# Pierwiastek całkowitoliczbowy z liczby naturalnej to część całkowita z pierwiastka z tej liczby.
# Proszę napisać program obliczający taki pierwiastek korzystając z zależności 1 + 3 + 5 + ... = n^2.

s = int(input("Sum = "))

curr_num = 1
n = 0
total = 0

while total <= s:
    total += curr_num
    n += 1
    curr_num += 2

print(n-1)