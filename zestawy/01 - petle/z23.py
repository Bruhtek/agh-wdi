# Proszę napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! +
# 1/1! + 1/2! + 1/3! + ...

def calc_euler()->float:
    e = 2
    divisor = 2
    mult_next = 3
    while 1/divisor > 0.0:
        e += 1/divisor
        divisor *= mult_next
        mult_next += 1

    return e


print(calc_euler())