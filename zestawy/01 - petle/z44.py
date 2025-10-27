
def sum_of_pow_n_digits(num, n)->int:
    sum = 0
    while num > 0:
        res = (num % 10) ** n
        sum += res
        num //= 10
    return sum


def largest_n(result)->int:
    n = len(str(result))
    test_num = (10 ** n) - 1
    while test_num > (10 ** (n - 1)):
        candidate = sum_of_pow_n_digits(test_num, n)
        if candidate == result:
            return test_num
        test_num -= 1
    return -1


print(largest_n(216))
print(largest_n(128))