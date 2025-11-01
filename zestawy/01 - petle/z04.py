# Proszę znaleźć wyrazy początkowe ciągu zamiast 1,1 o najmniejszej sumie, aby w ciągu
# analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku. - 2025

def has_target(a, b, target):
    while a <= target:
        if a == target:
            return True
        a, b = b, a + b
    return False

target = 2025

lowest_a, lowest_b = target, target

a = 1
while a <= target:
    b = 1
    while b <= target:
        total = a + b

        # Optimization
        if total > lowest_a + lowest_b:
            break

        if has_target(a, b, target):
            if total < lowest_a + lowest_b:
                print(f"Found starting values: {a}, {b} with sum {total}")
                lowest_a = a
                lowest_b = b
        b += 1
    a += 1

print(lowest_a, lowest_b, lowest_a + lowest_b)