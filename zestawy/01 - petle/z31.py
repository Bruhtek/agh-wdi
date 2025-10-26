# Zadanie 31. Proszę napisać program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale
# od 1 do k, metodą prostokątów.

def y(x)->float:
    return 1/x

def calc_area(k, step = 1e-3)->float:
    area = 0.0
    x = step
    while x < k - step:
        area += step * y(x)
        x += step
    return area


print(calc_area(100))
