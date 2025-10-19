# Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.

a = 1
b = 1

print(a)
while True:
    print(b)
    a, b = b, a + b
    if b > 1000000:
        break