# Proszę napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb naturalnych.

def lcd(a, b, c)->int:
    for i in range(1, a*b*c+1):
        if i % a == 0 and i % b == 0 and i % c == 0:
            return i

    return a*b*c

print(lcd(7,4,12))