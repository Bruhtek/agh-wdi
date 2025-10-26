# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta zawiera cyfrę równą liczbie swoich cyfr.
import math


def has_own_digit_count(n)->bool:
    digit_count = int(math.log10(n)) + 1
    if digit_count > 9:
        return False

    while n > 0:
        if digit_count == n % 10:
            return True
        n //= 10
    return False

print(has_own_digit_count(123))
print(has_own_digit_count(312))
print(has_own_digit_count(12))
print(has_own_digit_count(11))
print(has_own_digit_count(1111))