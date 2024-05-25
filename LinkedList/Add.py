class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class doublyLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def size(self) -> int:
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def append(self, elem):
        newnode = Node(elem, None, None)
        if self.isEmpty():
            self.__head = newnode
            self.__tail = newnode
        else:
            newnode.prev = self.__tail
            newnode.next = None
            self.__tail.next = newnode
            self.__tail = self.__tail.next
        self.__size += 1

    def addFirst(self, elem):
        newnode = Node(elem, None, None)
        if self.isEmpty():
            self.__head = newnode
            self.__tail = newnode
        else:
            newnode.next = self.__head
            newnode.prev = None
            self.__head.prev = newnode
            self.__head = self.__head.prev
        self.__size += 1

    def addInd(self, ind, elem):
        if ind < 0:
            raise Exception("Negative Index")

        if ind >= self.__size:
            raise Exception("Index Out of Bound")

        if ind == 0:
            self.addFirst()

        if ind == self.__size:
            self.append()

        trav = self.__head
        for _ in range(0, ind - 1):
            trav = trav.next

        newnode = Node(elem, None, None)

        newnode.next = trav.next
        newnode.prev = trav
        trav.next = newnode
        trav.next.prev = newnode
        
        self.__size+=1