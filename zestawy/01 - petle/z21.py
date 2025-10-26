# Dla ciągu z poprzedniego zadania proszę znaleźć najmniejszy wyraz początkowy N , dla
# którego ciąg osiąga wartość 1 dokładnie po N krokach.

def calc_steps(n)->int:
    steps = 0
    while n != 1:
        steps += 1
        n = (n % 2) * ((3 * n) + 1) + ((1 - n % 2) * n//2)

    return steps

wanted_steps = int(input("N = "))

i = 0
steps = -1
while steps != wanted_steps:
    i += 1
    steps = calc_steps(i)

print(i, steps)