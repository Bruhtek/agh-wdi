# Proszę napisać program znajdujący jak najwięcej liczb N -cyfrowych dla których suma N -
# tych potęg cyfr liczby jest równa tej liczbie, np. 153 = 1^3 + 5^3 + 3^3.
import random


def is_prime_fermat(n, tries=10)->bool:
    if n < 2:
        return False
    if n > 3 and (n % 2 == 0 or n % 3 == 0):
        return False

    for _ in range(tries):
        a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False

    return True


def check_all_for_n_digits(n: int)->None:
    num = 10 ** (n-1)
    if num % 2 == 0:
        num += 1 # have to be prime -> odd
    end = 10 ** n

    while num < end:
        sum = 0
        num_copy = num

        if not is_prime_fermat(num, 5):
            num += 2
            continue

        while num_copy > 0:
            digit = num_copy % 10
            num_copy //= 10
            sum += digit ** n

            # if bigger, no need to calculate further
            if sum > num:
                break

        if num == sum and is_prime_fermat(num, 50):
            print(num)

        num += 2

if __name__ == "__main__":
    for i in range(10):
        print("Checking for ", i, "digit numbers")
        check_all_for_n_digits(i)