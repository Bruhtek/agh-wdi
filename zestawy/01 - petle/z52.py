# Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej licz-
# bie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każ-
# dej z liczb wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby
# 12375, 17523, 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować
# z dwóch zadanych liczb.


import random


def is_prime_fermat(n, tries = 50)->bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True

    for _ in range(tries):
        a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False
    return True

def check_mask(mask, requested_count)->bool:
    ones_count = 0
    while mask > 0:
        if mask % 2 == 1:
            ones_count += 1
        mask //= 2

    return ones_count == requested_count

def combine_numbers(a, b, mask)->int:
    result = 0
    digit_count = 0
    requested_count = len(str(a)) + len(str(b))

    while digit_count != requested_count:
        if mask % 2 == 0:
            result += (a % 10) * (10 ** digit_count)
            a //= 10
        else:
            result += (b % 10) * (10 ** digit_count)
            b //= 10
        mask //= 2
        digit_count += 1

    return result

def prime_combinations(a, b)->int:
    length = len(str(a)) + len(str(b))

    count = 0
    for mask in range(1, 2**length):
        if check_mask(mask, len(str(b))):
            n = combine_numbers(a, b, mask)
            if is_prime_fermat(n):
                count += 1


    return count


print(prime_combinations(2, 71))