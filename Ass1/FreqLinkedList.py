class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.fre = 1


class FreqLinkedList:
    def __init__(self):
        self.head = Node("**dummy**")

    def printList(self):
        if self.head.next is not None:
            n = self.head.next
            while n.next is not None:
                print(n.data, n.fre)
                n = n.next
            print(n.data, n.fre)

    def addWord(self, word):
        new_node = Node(word)
        if self.head.next is None:
            self.head.next = new_node
            return

        prev = self.head
        n = prev.next
        while n is not None:
            if n.data > word:
                new_node.next = n
                prev.next = new_node
                return
            elif n.data == word:
                n.fre += 1
                return
            else:
                prev = n
                n = prev.next

        prev.next = new_node

    def filterWords(self, num):
        if self.head.next is not None:
            prev = self.head
            n = prev.next
            while n.next is not None:
                if n.fre < num:
                    prev.next = n = n.next
                    continue
                prev = prev.next
                n = prev.next
            if n.fre < num:
                prev.next = None
