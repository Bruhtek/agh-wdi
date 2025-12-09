# Zadanie 159. Problem wież w Hanoi (treść oczywista)

def hanoi(n, a, b, c):
    if n <= 0:
        return
    hanoi(n-1, a, c, b)
    print(f"{a} -> {c}")
    hanoi(n-1, b, a, c)

hanoi(4, "A", "B", "C")