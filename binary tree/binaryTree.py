class Node:
    def __init__(self, value = None):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class binaryTree:
    root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while(True):
                if val < current.value:
                    if current.leftChild == None:
                        current.leftChild = Node(val)
                        return
                    current = current.leftChild
                else:
                    if current.rightChild == None:
                        current.rightChild = Node(val)
                        return
                    current = current.rightChild

    def find(self, key):
        current = self.root
        while(current != None):
            if key < current.value:
                current = current.leftChild
            elif key > current.value:
                current = current.rightChild
            else:
                return 1
        return 0

    def traversePreOrder(self):
        self.__traversePreOrder(self.root)

    def __traversePreOrder(self, root):
        if root == None:
            return
        print(root.value)
        self.__traversePreOrder(root.leftChild)
        self.__traversePreOrder(root.rightChild)
    
    def traverseInOrder(self):
        self.__traverseInOrder(self.root)

    def __traverseInOrder(self, root):
        if root == None:
            return
        self.__traverseInOrder(root.leftChild)
        print(root.value)
        self.__traverseInOrder(root.rightChild)
    
    def traversePostOrder(self):
        self.__traversePostOrder(self.root)

    def __traversePostOrder(self, root):
        if root == None:
            return
        self.__traversePostOrder(root.leftChild)
        self.__traversePostOrder(root.rightChild)
        print(root.value)

    def height(self):
        print(self.__height(self.root))

    def __height(self, root):
        if root == None:
            return -1

        if root.leftChild == None and root.rightChild == None:
            return 0

        return 1 + max(self.__height(root.leftChild), self.__height(root.rightChild))

bt = binaryTree()

#INSERT
# bt.insert(10)
# bt.insert(5)
# bt.insert(20)
# bt.insert(15)
# bt.insert(25)

#FIND
# print(bt.find(20))

#TRAVERSE - PRE ORDER
# bt.traversePreOrder()

#TRAVERSE - IN ORDER
# bt.traverseInOrder()

#TRAVERSE - POST ORDER
# bt.traversePostOrder()

#HEIGHT
bt.height()