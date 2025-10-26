# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej
# cyfry stanowią ciąg rosnący.

def are_numbers_rising(n)->bool:
    # 123 - fits, which means that if we check if the numbers are getting smaller from the end, it works as well
    previous_num = n % 10
    while n > 0:
        n //= 10
        new_num = n % 10
        if new_num >= previous_num:
            return False

    return True

n = int(input("N = "))

print(n, are_numbers_rising(n))