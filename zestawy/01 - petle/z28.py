# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym

def is_palindrome(n) -> bool:
    n_copy = n
    rev = 0
    while n_copy > 0:
        rev *= 10
        rev += n_copy % 10
        n_copy //= 10

    return n == rev

def is_binary_palindrome(n) -> bool:
    n_copy = n
    rev = 0
    while n_copy > 0:
        rev *= 2
        rev += n_copy % 2
        n_copy //= 2

    print(n, rev)
    return n == rev

print(2137, is_palindrome(2137), is_binary_palindrome(2137))
print(71233217, is_palindrome(71233217), is_binary_palindrome(71233217))
print(21, is_palindrome(21), is_binary_palindrome(21))