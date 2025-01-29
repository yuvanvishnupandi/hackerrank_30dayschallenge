class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insert(self, head, data):
        new_node = Node(data)
        if head is None:
            return new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

mylist = Solution()
T = int(input())
head = None
for _ in range(T):
    data = int(input())
    head = mylist.insert(head, data)
    mylist.display(head)
