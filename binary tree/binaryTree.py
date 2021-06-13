import math

class Node:
    def __init__(self, value = None):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class binaryTree:
    root = None
    count = 0

    def insert(self, val):
        self.count += 1
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
        return self.__height(self.root)

    def __height(self, root):
        if root == None:
            return -1

        if root.leftChild == None and root.rightChild == None:
            return 0

        return 1 + max(self.__height(root.leftChild), self.__height(root.rightChild))

    def minBST(self):
        if self.root == None:
            raise Exception("Tree is empty")

        current = self.root
        while(current.leftChild != None):
            current = current.leftChild
        print(current.value)

    def minBT(self):
        print(self.__minBT(self.root))

    def __minBT(self, root):
        if root.leftChild == None or root.rightChild == None:
            return root.value

        left = self.__minBT(root.leftChild)
        right = self.__minBT(root.rightChild)

        return min(min(left, right), root.value)

    def equal(self, second):
        if second.root == None:
            print(0)
            return
        print(self.__equal(self.root, second.root))

    def __equal(self, first, second):
        if first == None and second == None:
            return 1
        if first != None and second != None:
            if first.value == second.value:
                tmp = self.__equal(first.leftChild, second.leftChild) and self.__equal(first.rightChild, second.rightChild)
                if tmp == None:
                    return 0
                else:
                    return tmp
            return 0

    def validate(self):
        print(self.__validate(self.root, -math.inf, math.inf))
    
    def __validate(self, root, min, max):
        if root == None:
            return 1
            
        if root.value < min or root.value > max:
            return 0

        return self.__validate(root.leftChild, -math.inf, root.value) and self.__validate(root.rightChild, root.value, math.inf)

    def nodesAtK(self, distance):
        if self.root == None:
            raise Exception("Tree is empty")

        self.__nodesAtK(self.root, distance)

    def __nodesAtK(self, root, distance):
        if root != None:
            if distance == 0:
                print(root.value)
                return
            
            self.__nodesAtK(root.leftChild, distance - 1)
            self.__nodesAtK(root.rightChild, distance - 1)

    def traverseLevelOrder(self):
        if self.root == None:
            raise Exception("Tree is empty")

        for i in range(self.height()+1):
            self.nodesAtK(i)
            
    def size(self):
        print(self.count)
        
    tmp = 0
    def countLeaf(self):
        if self.root != None:
            self.__countLeaf(self.root)
        print(self.tmp)
    
    def __countLeaf(self, root):
        if root == None:
            self.tmp += 1
            return
        self.__countLeaf(root.leftChild)
        self.__countLeaf(root.rightChild)

    def maxBT(self):
        print(self.__maxBT(self.root))
    
    def __maxBT(self, root):
        if root == None:
            return
        
        if root.leftChild == None or root.rightChild == None:
            return root.value
        
        left = self.__maxBT(root.leftChild)
        right = self.__maxBT(root.rightChild)

        return max(max(left, right), root.value)
        
    def contains(self, key):
        self.__contains(self.root, key)
    
    def __contains(self, root, key):
        if root == None:
            return
        
        if root.value == key:
            print("Found")
            return

        self.__contains(root.leftChild, key)
        self.__contains(root.rightChild, key)

    def areSibling(self, firstVal, secondVal):
        self.__areSibling(self.root, firstVal, secondVal)

    def __areSibling(self, root, firstVal, secondVal):
        if root == None:
            return

        if root.leftChild == None or root.rightChild == None:
            return

        if root.leftChild.value == firstVal and root.rightChild.value == secondVal:
            print("Yes")
            return
        
        self.__areSibling(root.leftChild, firstVal, secondVal)
        self.__areSibling(root.rightChild, firstVal, secondVal)

bt = binaryTree()

#INSERT
bt.insert(10)
bt.insert(5)
bt.insert(20)
bt.insert(1)
bt.insert(6)
bt.insert(15)
bt.insert(25)
bt.insert(8)

#FIND
# print(bt.find(20))

#TRAVERSE - PRE ORDER
# bt.traversePreOrder()

#TRAVERSE - IN ORDER
# bt.traverseInOrder()

#TRAVERSE - POST ORDER
# bt.traversePostOrder()

#HEIGHT
# print(bt.height())

#MIN IN A BINATY SEARCH TREE
# bt.minBST()

#MIN IN A BINATY TREE
# bt.minBT()

#EQUALITY CHECKING
# bt1 = binaryTree()
# bt1.insert(10)
# bt1.insert(5)
# bt1.insert(20)
# bt1.insert(15)
# bt1.insert(25)
# bt1.insert(1)
# bt1.insert(6)
# bt1.insert(8)

# bt.equal(bt1)

#VALIDATE
# bt.validate()

#PRINT NODES AT K FROM ROOT
# bt.nodesAtK(0)

#LEVEL ORDER TRAVERSAL
# bt.traverseLevelOrder()

#SIZE
# bt.size()

#COUNT LEAF NODES
# bt.countLeaf()

#MAXIMUM IN A BINARY TREE
# bt.maxBT()

#CONTAINS - BINARY TREE
# bt.contains(25)

#SIBLINGS
bt.areSibling(5, 20)