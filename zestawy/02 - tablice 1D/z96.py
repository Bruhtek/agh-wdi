# Dana jest tablica T zawierająca liczby naturalne. W tablicy na kolejnych pozycjach ukryto
# pewien ciąg liczb o długości co najmniej 3 elementów. Aby ułatwić odnalezienie tego ciągu, zaraz za nim
# umieszczono ten sam ciąg, ale każdy z jego elementów pomnożono przez pewną liczbę. Proszę napisać funkcję
# sequence(T) która odnajdzie ukryty ciąg. Funkcja powinna zwrócić indeksy pierwszego i ostatniego elementu
# ukrytego ciągu. Na przykład dla ciągu: 2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2 funkcja zwróci 4,7


def subseq(tab, start, stop)->list[int]:
    length = stop - start + 1
    res = [0 for _ in range(length)]
    for i in range(start, stop+1):
        res[i-start] = tab[i]
    return res

def sequence(T: list[int])->tuple[int,int]:
    n = len(T)
    for i in range(0, n-3):
        for j in range(i+3, n):
            seq_len = j-i
            if j + seq_len >= n:
                continue
            orig_seq = subseq(T, i, j-1)
            multiplied_seq = subseq(T, j, j + seq_len - 1)
            q = multiplied_seq[0] / orig_seq[0]
            passes = True
            for iter in range(seq_len):
                if orig_seq[iter] * q != multiplied_seq[iter]:
                    passes = False
                    break
            if passes:
                return (i, j-1)
    return (-1, -1)

print(sequence([2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]))