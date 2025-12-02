# Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.

from typing import  Generator

def possible_moves(tab_size, pos_x:int, pos_y:int)-> Generator[tuple[int, int]]:
    allowed_moves = [
        (-2, -1),
        (-2, 1),
        (2, 1),
        (2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2)
    ]

    for move in allowed_moves:
        res_x = pos_x + move[1]
        res_y = pos_y + move[0]

        if res_x < 0 or res_y < 0 or res_x >= tab_size or res_y >= tab_size:
            continue
        yield res_y, res_x

def solve(tab, n, pos_x, pos_y)-> list[list[int]] | bool:
    tab_size = len(tab)

    tab[pos_y][pos_x] = n

    if n == tab_size * tab_size:
        return tab
    for move in possible_moves(tab_size, pos_x, pos_y):
        if tab[move[0]][move[1]] != 0:
            continue

        solution = solve(tab, n+1, move[1], move[0])
        if solution != False:
            return solution

    tab[pos_y][pos_x] = 0
    return False


def generate_chessboard(n)->list[list[int]]:
    res = [[0 for _ in range(n)] for _ in range(n)]
    return res

def print_board(tab)->None:
    for verse in tab:
        for v in verse:
            print(v, end="\t")
        print("")
    print("")

board = generate_chessboard(5)
solution = solve(board, 1, 0, 0)
if solution == False:
    print("NO SOLUTIONS")
else:
    print_board(solution)