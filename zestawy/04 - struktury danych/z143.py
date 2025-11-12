# Zadanie 143. Dany jest ciąg N liczb naturalnych, z którego wybieramy spójny fragment o długości K
# (1 <K <N). Pomiędzy wszystkie elementy wybranego fragmentu możemy wstawiać operatory dodawania
# albo mnożenia, tak aby powstało wyrażenie arytmetyczne. W powstałym wyrażeniu nie mogą wystąpić dwa
# jednakowe operatory obok siebie. Interesuje nas znalezienie takiego fragmentu ciągu, który pozwala zbu-
# dować wyrażenie o wartości będącej liczbą pierwszą. Proszę napisać funkcję find max(T), która dla ciągu
# zawartego w tablicy T, wyznaczy wartość największej liczby pierwszej, jaką można znaleźć. Jeżeli taki pod-
# ciąg nie istnieje, funkcja powinna zwrócić wartość zero.
# Na przykład dla ciągu: 7,8,6,4,7,3 funkcja powinna zwrócić wartość 83
# Możliwe podciągi dające liczby pierwsze to:
# 7 + 8 ∗ 6 + 4 = 59
# 7 + 8 ∗ 6 + 4 ∗ 7 = 83
# 6 ∗ 4 + 7 = 31
# 4 + 7 = 11
import random


def is_prime_fermat(n, tries = 50):
    if n <= 2:
        return False
    if n == 2 or n == 3:
        return True

    for _ in range(tries):
        a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False
    return True

def calculate_values(seq: list[int])->tuple[int,int]:
    first_sum = seq[0]
    n = len(seq)
    for i in range(1, n-1, 2):
        first_sum += seq[i] * seq[i+1]
    if n % 2 == 0:
        first_sum += seq[n-1]

    second_sum = 0
    for i in range(0, n-1, 2):
        second_sum += seq[i] * seq[i+1]
    if n % 2 == 1:
        second_sum += seq[n-1]

    return first_sum, second_sum

def solve(T: list[int])->int:
    n = len(T)
    count = 0
    for i in range(0, n-1):
        for j in range(i+2, n):
            subseq = T[i:j]
            a1, a2 = calculate_values(subseq)
            if is_prime_fermat(a1):
                count += 1
            if is_prime_fermat(a2):
                count += 1
    return count

T = [7,8,6,4,7,3]
print(solve(T))