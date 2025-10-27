# Zadanie 43. Proszę napisać funkcję, która zwraca wartość True gdy dwie liczby są zbudowane z tych
# samych cyfr (na przykład: 123 i 231, 5749 i 4597) i wartość False w przeciwnym przypadku

def same_digits(a, b)->bool:
    digit_count = [0] * 10
    while a > 0:
        digit = a % 10
        digit_count[digit] += 1
        a //= 10
    while b > 0:
        digit = b % 10
        digit_count[digit] -= 1
        b //= 10

    for i in range(10):
        if digit_count[i] != 0:
            return False

    return True

print(same_digits(123, 321))
print(same_digits(123, 3321))
print(same_digits(5749, 4597))
print(same_digits(5749, 5597))