from itertools import permutations

def solve(n, equations):
    letters = set()
    for eq in equations:
        for char in eq:
            if char.isalpha():
                letters.add(char)

    letters = sorted(letters)
    num_letters = len(letters)

    if num_letters > 9:
        return "BRAK"

    parsed_equations = []
    for eq in equations:
        parts = eq.split('=', 1)
        addends = parts[0].split('+', 1)
        parsed_equations.append((addends[0], addends[1], parts[1]))

    for perm in permutations(range(1, 10), num_letters):
        letter_map = dict(zip(letters, perm))

        for arg1, arg2, result in parsed_equations:
            a = b = c = 0
            for ch in arg1:
                a = a * 10 + letter_map[ch]

            for ch in arg2:
                b = b * 10 + letter_map[ch]

            for ch in result:
                c = c * 10 + letter_map[ch]

            if a + b != c:
                break
        else:
            return ''.join(str(letter_map[letter]) for letter in letters)

    return "BRAK"

if __name__ == "__main__":
    n = int(input())
    equations = []
    for _ in range(n):
        equations.append(input().strip())

    print(solve(n, equations))
