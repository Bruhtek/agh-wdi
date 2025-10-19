# Największa liczba pierwsza:
# - 11-cyfrowa
# - palindrom
# - żadna cyfra nie pojawia się więcej niż 2 razy

import random

# using fermat test
def is_prime(n, tries = 100):
    if n < 2:
        return False
    for _ in range(tries):
        a = random.randint(1, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True


def make_palindrome(digits, center_twice = False):
    half = digits
    if center_twice:
        return half + half[::-1]
    else:
        return half + half[-2::-1]

def main():
    start_vals = [9, 8, 7, 6, 5, 4]
    palindrome = int(''.join([str(x) for x in make_palindrome(start_vals, False)]))
    if is_prime(palindrome):
        print("Found prime:", palindrome)
        return
    while True:
        for i in range(len(start_vals)-1, -1, -1):
            if start_vals[i] > 0:
                start_vals[i] -= 1
                break
            else:
                start_vals[i] = 9
        palindrome = int(''.join([str(x) for x in make_palindrome(start_vals, False)]))
        if is_prime(palindrome):
            print("Found prime:", palindrome)
            # return


if __name__ == "__main__":
    main()