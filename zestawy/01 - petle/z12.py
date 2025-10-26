# Proszę napisać program wypisujący podzielniki liczby

def divisors(n)->None:
    div = 1
    while div*div <= n:
        if n % div == 0:
            print(div)
            if div*div != n:
                print(n//div)
        div += 1


divisors(23)