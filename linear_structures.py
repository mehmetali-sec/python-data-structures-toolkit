class Stack:
    def __init__(self):
        self.__items = []  # Private yaparak dışarıdan erişimi kısıtladık

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        return self.__items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.__items.pop(0)
        raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        return len(self.__items) == 0

class Deque:
    def __init__(self):
        self.__items = []

    def add_front(self, item):
        self.__items.insert(0, item)

    def add_rear(self, item):
        self.__items.append(item)

    def remove_front(self):
        return self.__items.pop(0)

    def remove_rear(self):
        return self.__items.pop()

    def is_empty(self):
        # Senin kodunda 'self.items == None' idi, bu hatayı düzelttik
        return len(self.__items) == 0
