from typing import Any, Generator


def letter_count(equations: list[str])->int:
    highest_letter = 0
    for eq in equations:
        for letter in eq:
            if letter == "=" or letter == "+":
                continue
            val = ord(letter) - ord("A")
            highest_letter = max(highest_letter, val)
    return highest_letter + 1

def letter_value(letter: str, resolutions: list[int]):
    return resolutions[ord(letter) - ord("A")]

def solve_equation(eq: str, res: list[int])->int:
    a = 0
    b = 0
    c = 0
    iter = 0
    if letter_value(eq[iter], res) == 0: return False
    while iter < len(eq):
        letter = eq[iter]
        if letter == "+":
            iter += 1
            break
        a = 10 * a + letter_value(letter, res)
        iter += 1
    if letter_value(eq[iter], res) == 0: return False
    while iter < len(eq):
        letter = eq[iter]
        if letter == "=":
            iter += 1
            break
        b = 10 * b + letter_value(letter, res)
        iter += 1
    if letter_value(eq[iter], res) == 0: return False
    while iter < len(eq):
        letter = eq[iter]
        c = 10 * c + letter_value(letter, res)
        iter += 1
    return a + b == c


def equations_work(equations: list[str], resolutions: list[int])->int:
    for eq in equations:
        if not solve_equation(eq, resolutions):
            return False
    return True

def permutations(head, tail=None)-> Generator[list[int]]:
    if tail is None:
        tail = []
    if len(head) == 0:
        yield tail
    else:
        for i in range(len(head)):
            for perm in permutations(head[:i] + head[i+1:], tail + [head[i]]):
                yield perm


if __name__ == "__main__":
    n = int(input())
    equations = [input() for _ in range(n)]

    lc = letter_count(equations)
    resolution_tab = [i for i in range(10)] # all possible combinations, we're only using a subset
    solved = equations_work(equations, resolution_tab)
    solution = None
    for res in permutations(resolution_tab):
        solved = equations_work(equations, res)
        if solved:
            if solution is None:
                solution = ''.join([str(x) for x in res[0:lc]])
            else:
                solution = None
                print("BRAK")
                break
    if solution is not None:
        print(solution)