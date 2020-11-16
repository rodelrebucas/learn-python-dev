"""
    TODO
    Pre order: node, left, right
"""


class BinaryTreePreOrderTree(object):
    raise NotImplemented


"""
    Inorder (LNR) - left, node, right
    Time Complexity: O(log(N)), balanced tree O(n)
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:  # insert first node
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)  # insert succeeding nodes

    def remove(self, data):
        # make sure your tree contains data
        if self.root:
            self.root = self.removeNode(data, self.root)  # return the updated nodes

    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:  # traverse to the existing left child
                self.insertNode(data, node.leftChild)
            else:  # set left child
                node.leftChild = Node(data)
        else:
            if node.rightChild:  # traverse to the existing right child
                self.insertNode(data, node.rightChild)
            else:  # set right child
                node.rightChild = Node(data)

    def removeNode(self, data, node):

        # an empty node, not found
        if not node:
            print("data not found...")
            return node
        # recurse left
        elif data < node.data:
            # set node as left child whatever children the removed node have
            node.leftChild = self.removeNode(data, node.leftChild)
        # recurce right
        elif data > node.data:
            # set node as left child whatever children the removed node have
            node.rightChild = self.removeNode(data, node.rightChild)
        # data == node.data
        else:
            # node is a leaf node
            if not node.leftChild and not node.rightChild:
                del node
                return None
            # node has only right child
            if not node.leftChild:
                tempNode = node.rightChild
                del node
                return tempNode
            # node has only left child
            elif not node.rightChild:
                tempNode = node.leftChild
                del node
                return tempNode

            # node has both right and left child
            # get the predecessor or the highest on left child
            # OR get successor the node after the target node

            # succesor method
            tempNode = self.getPredecessor(node.leftChild)
            # replace the data from the predecessor
            node.data = tempNode.data
            # delete the predecessor node, recurse
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
        return node

    def getPredecessor(self, node):

        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)

        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)

        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:  # if a left child exist traverse
            self.traverseInOrder(node.leftChild)

        # print current root node
        print(node.data)

        if node.rightChild:  # if a right child exist traverse
            self.traverseInOrder(node.rightChild)


if __name__ == "__main__":

    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(13)
    bst.insert(5)
    bst.insert(14)

    print(f"Max value: { bst.getMaxValue()}")
    print(f"Min value: {bst.getMinValue()}")
    print(bst.traverse())

    num = 100
    print(f"Removing {num}")
    bst.remove(num)

    print(f"Max value: { bst.getMaxValue()}")
    print(f"Min value: {bst.getMinValue()}")
    print(bst.traverse())


"""
    TODO
    Post order: left, right, node
"""


class BinaryTreePostOrderTree(object):
    raise NotImplemented
