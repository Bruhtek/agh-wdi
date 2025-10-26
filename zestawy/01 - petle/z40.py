# Zadanie 40. Napisać program, który wyznacza liczbę zer jakimi kończy się liczba N ! Program powinien
# działać dla N rzędu 10100.

def count_zeros(n)->int:
    count = 0

    div = 5
    while div <= n:
        count += n//div
        div *= 5

    return count

print(count_zeros(25))
print(count_zeros(125))