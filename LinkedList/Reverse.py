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

    def __len__(self):
        return self.__size

    def size(self) -> int:
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def peekFirst(self):
        if self.isEmpty():
            return "Empty List"
        return self.__head.data

    def peekLast(self):
        if self.isEmpty():
            return "Empty List"
        return self.__tail.data

    def indexOf(self, data):

        trav = self.__head
        index = 0

        while trav is not None:
            if trav.data == data:
                return index

            index += 1
            trav = trav.next

        return -1

    def contains(self, data):
        return self.indexOf(data) != -1

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
        
    def reverse(self):
        prev = None
        curr = self.__head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.__head = prev
        
l=doublyLL()
l.append(Node(5))
l.append(Node(6))
l.append(Node(7))
print(len(l))
curr = l._doublyLL__head
while curr:
    print(curr.data)
    curr = curr.next
