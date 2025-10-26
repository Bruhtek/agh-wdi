# Proszę napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.
# cos(x) = ∑∞ (−1)n/(2n)! x2n

import math

x = float(input("X (in rad) = "))
sum = 1
s = 0
w = 1
while w != 0:
    w = -(w*x*x)/((s+1) * (s+2))
    sum += w
    s += 2

print(math.cos(x))
print(sum)