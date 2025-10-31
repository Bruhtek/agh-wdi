# Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
# naturalnymi po spirali.

n = int(input("N = "))
T = [[0] * n for _ in range(n)]

def print_tab(tab):
    for t in tab:
        for item in t:
            print(item, end="\t")
        print()

direction_x = 1
direction_y = 0

x = 0
y = 0

min_x = -1
max_x = n
min_y = -1
max_y = n

i = 1

while i <= n*n:
    T[y][x] = i
    x += direction_x
    y += direction_y
    i += 1

    if x == max_x:
        x = max_x - 1
        direction_x = 0
        direction_y = 1
        min_y += 1
        y += 1

    if x == min_x:
        x = min_x + 1
        direction_x = 0
        direction_y = -1
        max_y -= 1
        y -= 1

    if y == max_y:
        y = max_y - 1
        direction_x = -1
        direction_y = 0
        max_x -= 1
        x -= 1

    if y == min_y:
        y = min_y + 1
        direction_x = 1
        direction_y = 0
        min_x += 1
        x += 1



print_tab(T)