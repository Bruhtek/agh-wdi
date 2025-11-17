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

    parsed_equations: list[tuple[str, str, str]] = []
    for eq in equations:
        parts = eq.split('=')
        left = parts[0]
        right = parts[1]

        addends = left.split('+')
        parsed_equations.append((addends[0], addends[1], right))

    for perm in permutations(range(1, 10), num_letters):
        letter_map = dict(zip(letters, perm))

        valid = True
        for arg1, arg2, result in parsed_equations:
            num1 = int(''.join(str(letter_map[c]) for c in arg1))
            num2 = int(''.join(str(letter_map[c]) for c in arg2))
            expected_result = int(''.join(str(letter_map[c]) for c in result))

            if num1 + num2 != expected_result:
                valid = False
                break

        if valid:
            solution = ''.join(str(letter_map[letter]) for letter in letters)
            return solution

    return "BRAK"


if __name__ == "__main__":
    n = int(input())
    equations = []
    for _ in range(n):
        equations.append(input().strip())

    print(solve(n, equations))
