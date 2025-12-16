# Zadanie 189. Proszę zaimplementować zbiór mnogościowy liczb naturalnych korzystając ze struktury listy odsyłaczowej.
# • czy element należy do zbioru
# • wstawienie elementu do zbioru
# • usunięcie elementu ze zbioru

class Node:
    value = 0
    next: "Node|None" = None

    def __init__(self, value=0):
        self.value = value
        self.next = None

class Set:
    first: Node|None = None
    power: int = 0

    def __init__(self):
        self.first = None
        self.power = 0

    def contains(self, x: int):
        p = self.first
        while p is not None:
            val = p.value
            if val == x:
                return True
            if val > x:
                break
        return False

    def insert(self, x: int):
        p = self.first
        prev = None
        if p is None:
            self.first = Node(x)
            self.power = 1
            return

        while p is not None and p.value < x:
            prev = p
            p = p.next

        if p is not None and p.value == x:
            return

        n = Node(x)
        n.next = p
        n.next = p
        self.power += 1
        if prev is None:
            self.first = n
            return

        prev.next = n


    def delete(self, x: int)->bool:
        p = self.first
        prev = None
        while p is not None and p.value < x:
            prev = p
            p = p.next

        if p is None or p.value != x:
            return False

        self.power -= 1
        if prev is None:
            self.first = p.next
            del p
            return True

        prev.next = p.next
        del p
        return True


    def elements(self):
        p = self.first
        while p is not None:
            yield p.value
            p = p.next

    def __repr__(self):
        elements = [str(val) for val in self.elements()]
        return ",".join(elements)

s = Set()
s.insert(1)
s.insert(2)
s.insert(30)
s.insert(5)
s.insert(0)
s.insert(2)
s.insert(1)
s.insert(30)
print(s, s.power)
s.delete(0)
s.delete(2)
s.delete(30)
print(s, s.power)