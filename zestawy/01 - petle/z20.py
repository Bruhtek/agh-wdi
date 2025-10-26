# Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Proszę napisać program, który znajdzie
# wyraz początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.

def calc_steps(n)->int:
    steps = 0
    while n != 1:
        steps += 1
        n = (n % 2) * ((3 * n) + 1) + ((1 - n % 2) * n//2)

    return steps

greatest = 0
greatest_num = -1
for i in range(2, 10001):
    steps = calc_steps(i)
    if steps > greatest:
        greatest = steps
        greatest_num = i

print(greatest_num, "steps:", greatest)