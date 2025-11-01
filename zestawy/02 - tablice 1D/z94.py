# Proszę napisać program, który wyznacza wartość pierwiastka kwadratowego z liczby natu-
# ralnej x z dokładnością do N miejsc dziesiętnych po przecinku. Program powinien działać poprawnie dla
# x<10^8 i N <100 .

def square_tab(tab)->list[int]:
    n = len(tab)
    res = [0 for _ in range(n*2)]
    for i in range(n):
        for j in range(n):
            res[i+j] += tab[i] * tab[j]

    for i in range(n*2-1,0, -1):
        curr = res[i]
        if curr > 9:
            carry = curr // 10
            res[i-1] += carry
            res[i] %= 10
    return res

def sroot(x, n):
    res = [0 for _ in range(n+2)]
    res[0] = 1
    while square_tab(res)[0] <= x:
        res[0] += 1
    res[0] -= 1

    for i in range(1, n+2):
        for digit in range(1, 10):
            res[i] = digit
            if square_tab(res)[0] >= x:
                res[i] -= 1
                break
    print(res)


print(sroot(111, 30))