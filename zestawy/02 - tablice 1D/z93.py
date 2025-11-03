# Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
# różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np.
# dla 2315 będą to 21, 35, 231, 315.
import math

def digit_count(n)->int:
    if n == 0: return 0
    return int(math.log10(n)) + 1

def get_num(n, mask)->int:
    res = 0
    while mask > 0:
        if mask % 2 == 1:
            res = (n % 10) * (10 ** digit_count(res)) + res
        n //= 10
        mask //= 2
    return res

def count_div_by_7(n)->int:
    divisible = 0
    for mask in range(2**digit_count(n)):
        if mask == 0:
            continue
        num = get_num(n, mask)
        if num % 7 == 0:
            divisible += 1
    return divisible

print(count_div_by_7(2315))