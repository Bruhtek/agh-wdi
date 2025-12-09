# Zadanie 170. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A
# cyfr 1 oraz B cyfr 0, gdzie A,B >0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca
# ilość wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2),10100(2),11000(2)
import random


def check(num)->bool:
    if num <= 3:
        return False
    if num % 2 == 0:
        return True

    for _ in range(50):
        a = random.randint(1, num-1)
        if pow(a, num-1, num) != 1:
            return True
    return False

def how_many(num: int, a: int, b: int)->int:
    if a == 0 and b == 0:
        if check(num):
            print(num)
            return 1

    sum = 0
    if a > 0:
        sum += how_many(num * 2 + 1, a-1, b)
    if b > 0:
        sum += how_many(num * 2, a, b-1)
    return sum

a = int(input("A = ")) - 1
b = int(input("B = "))

print(how_many(1, a, b))

