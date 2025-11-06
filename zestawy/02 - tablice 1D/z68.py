# Zadanie 68. Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakoń-
# czonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
# wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.

num=int(input())
biggest = [-1 for _ in range(10)]
while num != 0:
    iter = 0
    while iter <= 9 and biggest[iter] >= num:
        iter += 1
    if iter <= 9:
        for i in range(9, iter, -1):
            biggest[i] = biggest[i-1]
        biggest[iter] = num

    num = int(input())

print(biggest[9])