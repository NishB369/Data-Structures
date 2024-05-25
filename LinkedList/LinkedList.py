class Node:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

class SLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def append_at_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        self.size += 1

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        new_node = Node(data)
        if index == 0:
            self.add_first(data)
        elif index == self.size:
            self.append_at_last(data)
        else:
            pos = self.head
            for _ in range(index - 1):
                pos = pos.next
            next_pos = pos.next
            pos.next = new_node
            new_node.next = next_pos
            self.size += 1

    def del_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            next_head = self.head.next
            self.head.next = None
            self.head = next_head
            self.size -= 1
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            cur_next = current.next.next
            current.next.next = None
            current.next = cur_next
            self.size -= 1

    def middle(self):
        if self.is_empty():
            return -1
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def index_at(self, data):
        current = self.head
        index = 0
        while current:
            if current.val == data:
                return index
            current = current.next
            index += 1
        return -1

    def merge_two_lists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return head

    def interleave(self, list1, list2):
        l1 = list1
        l2 = list2
        while l1 and l2:
            l1p = l1.next
            l2p = l2.next
            l1.next = l2
            l2.next = l1p
            l1 = l1p
            l2 = l2p
        return list1

    def two_parts(self, head, index):
        list2 = head
        for _ in range(index - 1):
            list2 = list2.next
        random = list2.next
        list2.next = None
        return random

    def rotate(self, k):
        diff = k % self.size
        if diff == 0:
            return
        move = self.size - diff
        rot = self.head
        for _ in range(move - 1):
            rot = rot.next
        rot2 = rot.next
        rot.next = None
        rot3 = rot2
        while rot3.next:
            rot3 = rot3.next
        rot3.next = self.head
        self.head = rot2

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=' ')
            current = current.next
        print()


