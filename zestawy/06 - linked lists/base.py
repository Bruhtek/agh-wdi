class Node:
    value = None
    next: "Node|None" = None

    def __init__(self, value = None):
        self.value = value
        self.next = None
