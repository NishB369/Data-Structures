class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.__size = 0
        self.__head = None

    def size(self) -> int:
        return self.__size

    def isEmpty(self) -> bool:
        return self.size() == 0

    def push(self, val: int) -> None:
        newnode = Node(val, None)
        if self.isEmpty():  # not necessary to handle
            self.__head = newnode
        else:
            newnode.next = self.__head
            self.__head = newnode
        self.__size += 1

    def pop(self) -> int:
        if self.isEmpty():
            raise Exception("Stack Underflow")
        else:
            data = self.__head.data
            temp = self.__head
            self.__head = self.__head.next
            del temp
        self.__size -= 1
        return data

    def top(self):
        if self.isEmpty():
            raise Exception("Stack Underflow")
        return self.__head.data

    def __str__(self):
        st=[]
        trav=self.__head
        while trav:
            st.append(str(trav.data))
            trav=trav.next
        return '->'.join(st)
    
st=Stack()
st.push(5)
st.push(10)
st.push(12)
print(st)
print(st.pop())
print(st)