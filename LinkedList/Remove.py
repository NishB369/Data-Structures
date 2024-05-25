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

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Empty List")

        self.__head = self.__head.next
        self.__size -= 1

        if self.isEmpty():
            self.__tail = None
        else:
            self.__head.prev = None

    def removeLast(self):
        if self.isEmpty():
            raise Exception("Empty List")

        self.__tail = self.__tail.prev
        self.__size -= 1

        if self.isEmpty():
            self.__head = None
        else:
            self.__tail.next = None

            raise Exception("Empty List")

    def __remove__(self, node):

        if node.prev == None:
            self.removeFirst()
            return

        if node.next == None:
            self.removeLast()
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        del node
        self.__size -= 1
        return None

    def removeAt(self, index):

        if index < 0 or index >= self.__size:
            raise Exception("Invalid index")

        trav = self.__head
        i = 0
        while i != index:
            trav = trav.next
            i += 1

        return self.__remove__(trav)
