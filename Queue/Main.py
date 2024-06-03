class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
        
class Queue:
    def __init__(self):
        self.__size=0
        self.__head=None
        self.__tail=None
        
    def size(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size==0
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.__head.data
    
    def dequeue(self, data):
        if self.isEmpty():
            raise Exception("Empty Queue")
        else:
            temp=self.__head
            self.__head=self.__head.next
            data=temp.data
            del temp
            self.__size-=1
            return data
    
    def enqueue(self, data):
        new_node=Node(data)
        if self.isEmpty():
            self.__head=self.__tail=new_node 
        else:
            self.__tail.next=new_node
            self.__tail=new_node
        self.__size+=1
            
    def __str__(self) -> str:
        return str(self.__data[:self.__size])
            
    
l=Queue()
print(l.size())
print(l.peek())
l.enqueue(5)
print(l.size())
print(l.peek())
