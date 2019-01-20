"""
    Linked lists are nodes connected with one another by
    containing the references of the next node and the previos node

    Time complexity
            Start   End
    Insert  O(1)    O(n)
    Remove  O(1)    O(n) 

"""


class Node(object):
    def __init__(self, data):
        self.data = data
        # Use this if you want double linked list,
        # and avoid tracking previous node with a temporary pointer
        self.prev_node = None

        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        self.size = self.size + 1

        # Create a new node
        node = Node(data)

        # first insertion
        # set the head of the linked list
        # to the first node
        if not self.head:
            self.head = node
        else:  # succeding insertions
            # point next node to self.head
            # since this is the curret node
            node.next_node = self.head

            # point the  head to the new node
            self.head = node

    def insertEnd(self, data):
        self.size = self.size + 1
        node = Node(data)

        # create a copy for iterationa
        head = self.head

        # iterate until the last node
        while head.next_node is not None:
            head = head.next_node

        # insert node
        head.next_node = node

    def remove(self, data):

        curr = self.head
        prev = None

        # iterate until match is found
        while curr.data != data:
            prev = curr
            # Searching for a non existing data
            # raises AttributeError on curr.data
            # since at the end of Node , there is no existing node
            # so get next node only if next is a Node
            # else break
            if curr.next_node is not None:
                curr = curr.next_node
            else:
                break
        # meaning data is found at first node
        # no iteration happened
        # so prev is None
        # set the head to the next node
        if prev is None:
            self.head = curr.next_node
            self.size = self.size - 1
        else:  # iterations happened
            # point the previos node
            # to the current 's next node
            # Note: self.head is already pointed to the previous node
            prev.next_node = curr.next_node
            self.size = self.size - 1

    # O(1)
    # since we keep track of the size nevery node creation
    def size1(self):
        return self.size

    # O(n)
    # counting the node
    def size2(self):
        head = self.head

        while not head.next_node:
            self.size = self.size + 1
            # get the next node
            head = head.next_node

        return self.size

    # traversal
    def traverse(self):
        head = self.head

        # traverse until there is no Node
        while head is not None:
            print(head.data)
            head = head.next_node


if __name__ == "__main__":
    linkedList = LinkedList()

    linkedList.insertStart("a")
    linkedList.insertStart("b")
    linkedList.insertStart("c")
    linkedList.insertStart("d")

    linkedList.traverse()
    print("Size:", linkedList.size1())

    linkedList.remove("t")
    linkedList.traverse()
    print("Size:", linkedList.size2())
