# Zadanie 191. Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę. Do
# funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wskazanie do
# scalonej listy. Zadanie należy wykonać jako funkcję iteracyjną, a następnie jako funkcję rekurencyjną

class Node:
    value: int = 0
    next: "Node|None" = None
    def __init__(self, value = 0):
        self.value = value
        self.next = None

    def elements(self):
        p = self
        while p is not None:
            yield p.value
            p = p.next
    def __repr__(self):
        return ','.join(str(el) for el in self.elements())

def insert_at_end(value: int, c: Node)->Node:
    b = Node(value)
    c.next = b
    return b

def from_list(values: list[int])->Node|None:
    if len(values) == 0: return None
    first = Node(values[0])
    curr = first
    for val in values[1:]:
        n = Node(val)
        curr.next = n
        curr = n
    return first

def merge_sorted(a: Node, b: Node)->Node:
    if a is None:
        return b
    if b is None:
        return a

    if a.value < b.value:
        first = Node(a.value)
        a = a.next
    else:
        first = Node(b.value)
        b = b.next

    curr = first
    while a is not None and b is not None:
        if a.value < b.value:
            curr = insert_at_end(a.value, curr)
            a = a.next
        else:
            curr = insert_at_end(b.value, curr)
            b = b.next

    if a is None:
        curr.next = b
    else:
        curr.next = a

    return first

a = from_list([2,4,5,6,8,10])
b = from_list([1,3,5])
print(merge_sorted(a, b))