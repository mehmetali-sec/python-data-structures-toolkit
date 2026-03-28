class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        """Listenin başına ekleme yapar (O(1))"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get_element_at(self, index):
        """Belirtilen index'teki elemanı döndürür (1 tabanlı)"""
        current = self.head
        count = 1
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        return None

    def __str__(self):
        """Listeyi ekrana düzgün yazdırmak için özel metod"""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)
