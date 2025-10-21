# Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.

def change_base(n, base = 2)->str:
    res = ""
    while n > 0:
        val = n % base
        char = str(val)
        if val > 9:
            chars = ['A', 'B', 'C', 'D', 'E', 'F']
            char = chars[val-10]

        res = char + res
        n //= base
    return res

print(change_base(31, 2))
print(change_base(32, 2))
print(change_base(31, 16))