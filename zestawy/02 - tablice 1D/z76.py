# Proszę napisać program, który wypełnia N-elementową tablicę T trzycyfrowymi liczba-
# mi pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdujące-
# go się w tablicy dla którego w tablicy występuje również rewers tego ciągu. Na przykład dla tablicy: t=
# [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4.

def reverse(tab)->list[int]:
    n = len(tab)
    res = [0 for _ in range(n)]
    for i in range(n):
        res[n-1-i] = tab[i]
    return res

def contains_subseq(tab, subseq)->bool:
    n = len(tab)
    k = len(subseq)
    for i in range(n):
        if tab[i] == subseq[0]:
            flag = True
            for j in range(0, k):
                if i+j >= n:
                    flag = False
                    break
                if tab[i+j] != subseq[j]:
                    flag = False
                    break
            if flag:
                return True
    return False

def get_subseq(tab, start, end)->list[int]:
    n = end - start + 1
    res = [0 for _ in range(n)]
    for i in range(0, n):
        res[i] = tab[start+i]
    return res

def longest_that_has_reverse(tab: list[int])->int:
    n = len(tab)
    longest = 1
    for i in range(n):
        for j in range(1,n-i):
            subseq = get_subseq(tab, i, i+j)
            if contains_subseq(tab, reverse(subseq)):
                longest = max(longest, len(subseq))
    return longest


print(longest_that_has_reverse([2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]))