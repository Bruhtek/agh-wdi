# Napisać program, który wyznacza ostatnia niezerową cyfrę liczby N !. Program powinien
# działać dla N rzędu 10^100. Komentarz: Rozwiązanie tego zadania w języku Python jest proste, trochę więk-
# szym wyzwaniem jest rozwiązanie w języku C/C++

n = int(input("N = "))

def last_nonzero_digit(n):
    while n % 10 == 0:
        n //= 10
    return n % 10

digit_for_10 = last_nonzero_digit(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10)

res = 1
while n > 10:
    digit_for = 10
    digit = digit_for_10
    while n // 10 > digit_for:
        digit = last_nonzero_digit(digit ** 10)
        digit_for *= 10
    n -= digit_for
    res = last_nonzero_digit(res * digit)

digit = 1
while n > 0:
    res *= digit
    digit += 1
    n -= 1

print(last_nonzero_digit(res))