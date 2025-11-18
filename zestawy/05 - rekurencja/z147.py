# Zadanie 147. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi
# zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i
# kolumnie k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy
# minimalny koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt
# przebywania na polu startowym i ostatnim także wliczamy do kosztu przejścia.

def min_cost(tab: list[list[int]], k: int, y: int, current_cost: int = 0)->int:
    current_cost += tab[y][k]

    if y == 7: return current_cost

    costs = [9999999,9999999,9999999]
    if k > 0:
        costs[0] = min_cost(tab, k-1, y+1, current_cost)
    if k < 7:
        costs[1] = min_cost(tab, k+1, y+1, current_cost)
    costs[2] = min_cost(tab, k, y+1, current_cost)

    return min(costs)

def solve(tab: list[list[int]], k: int)->int:
    cost = min_cost(tab, k, 0, 0)
    return cost

T1 = [
    [5, 3, 2, 8, 4, 6, 7, 9],
    [4, 2, 1, 5, 3, 7, 8, 6],
    [6, 3, 2, 4, 2, 5, 9, 7],
    [5, 4, 1, 3, 2, 6, 8, 5],
    [7, 5, 2, 2, 1, 4, 7, 6],
    [6, 4, 3, 1, 2, 5, 8, 7],
    [8, 5, 4, 2, 3, 6, 9, 8],
    [9, 6, 5, 3, 4, 7, 8, 9],
]
k1 = 2  # kolumna startowa
print(solve(T1, k1))