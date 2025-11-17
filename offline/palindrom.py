from typing import Any


def is_palindrome(text: str)->bool:
    n = len(text)
    for i in range(n//2 + 1):
        if text[i] != text[n-i-1]:
            return False
    return True

PALINDROME_MIN_SIZE=5

def find_palindrome(verse: str)-> str|None:
    n = len(verse)
    longest = None
    max_length = 0

    for i in range(n - 4):
        for j in range(i + 4, n):
            sub_verse = verse[i:j + 1]
            if is_palindrome(sub_verse):
                if len(sub_verse) > max_length:
                    longest = sub_verse
                    max_length = len(sub_verse)

    return longest


def find_all_crosses(tab: list[str])->list[str]:
    n = len(tab)
    res = []
    for i in range(n):
        cross = ""
        j = 0
        while i < n and j < n:
            cross += tab[i][j]
            j += 1
            i += 1
        if len(cross) >= 5:
            res.append(cross)
    for j in range(1, n):
        cross = ""
        i = 0
        while i < n and j < n:
            cross += tab[i][j]
            j += 1
            i += 1
        if len(cross) >= 5:
            res.append(cross)

    return res

def find_all_anti_crosses(tab: list[str]) -> list[str]:
    n = len(tab)
    res = []

    for col in range(n):
        anti_diag = ""
        row, c = 0, col
        while row < n and c >= 0:
            anti_diag += tab[row][c]
            row += 1
            c -= 1
        if len(anti_diag) >= 5:
            res.append(anti_diag)

    for row in range(1, n):
        anti_diag = ""
        r, col = row, n - 1
        while r < n and col >= 0:
            anti_diag += tab[r][col]
            r += 1
            col -= 1
        if len(anti_diag) >= 5:
            res.append(anti_diag)

    return res


def main()->str:
    n = int(input())
    tab = [input() for _ in range(n)]
    verses = find_all_crosses(tab) + find_all_anti_crosses(tab) + tab + [''.join([tab[i][j] for i in range(n)]) for j in range(n)]
    palindromes = {}
    for verse in verses:
        pali = find_palindrome(verse)
        if pali is not None:
            if pali in palindromes:
                return pali
            else:
                palindromes[pali] = 1
    return "NONE"

if __name__ == "__main__":
    print(main())