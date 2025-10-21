# Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa
import math


def sieve(n)->None:
    # 1 - prime
    # 0 - not prime
    numbers = [1 for _ in range(n+1)]
    numbers[0] = 0
    numbers[1] = 0

    i = 2
    while i*i <= n:
        for j in range(i*i, n+1, i):
            numbers[j] = 0

        i += 1

    for index, x in enumerate(numbers):
        if x == 1:
            print(index, end=" ")

sieve(100)