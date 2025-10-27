# Proszę napisać funkcję, która sprawdza czy napis składający się z: liter a..z, operatorów
# dodawania i mnożenie oraz nawiasów jest poprawnym wyrażeniem arytmetycznym.

wyr = str(input("Wyrazenie: "))

token_chars = 'abcdefghijklmnopqrstuwxyz123456789'
operator_chars = '+*'
bracket_start = '('
bracket_end = ')'

in_token = False
nested_count = 0

def incorrect(where, why)->None:
    print("INCORRECT!")
    print(wyr)
    print((" " * (where-1)) + "^ HERE")
    print()
    print(why)
    exit(1)

for i in range(len(wyr)):
    char = wyr[i]
    if in_token:
        if char in operator_chars:
            in_token = False
        if char == bracket_end:
            nested_count -= 1
            if nested_count < 0:
                incorrect(i, "Too few brackets")

        # assuming that a(b+a) is allowed
        if char == bracket_start:
            nested_count += 1

        # else, it was just a token, ignore it - assuming that abc*3 is allowed and means a*b*c*3
    else:
        if char in operator_chars:
            incorrect(i, "Two operators after each other")
        if char in token_chars:
            in_token = True
            continue
        if char == bracket_end:
            incorrect(i, "Bracket end after an operator")
        if char == bracket_start:
            in_token = True
            nested_count += 1
            continue


if nested_count > 0:
    incorrect(len(wyr), "Too many brackets")

print("PASSES!")