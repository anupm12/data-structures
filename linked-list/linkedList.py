class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class linkedList:
    first = None
    last = None
    count=0

    def isEmpty(self):
        return self.first == None

    def print(self):
        current = self.first
        while(current != None):
            print(current.value)
            current = current.next

    def addLast(self, value):
        node = Node(value)
        if(self.isEmpty()):
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.count+=1
        
    def addFirst(self, value):
        node = Node(value)
        if(self.isEmpty()):
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node
        self.count+=1
    
    def indexOf(self, value):
        current = self.first
        i=0
        while(current != None):
            if(current.value == value):
                return i-1
            current = current.next
            i+=1
        return -1

    def contains(self, value):
        return self.indexOf(value) != -1

    def removeFirst(self):
        if(self.isEmpty()):
            print("Linked list empty")
        elif(self.first == self.last):
            self.first = None
            self.last = None
        else:
            current = self.first
            self.first = self.first.next
            current.next = None
        self.count-=1

    def removeLast(self):
        if(self.isEmpty()):
            print("Linked list empty")
        elif(self.first == self.last):
            self.first = None
            self.last = None
        else:
            current = self.first
            while(current != None):
                if(current.next == self.last):
                    self.last = current.next
                    current.next = None
                current = current.next
        self.count-=1

    def size(self):
        return self.count
    
    def toArray(self):
        if(self.isEmpty()):
            print("Linked list empty")
        current = self.first
        a = []
        while(current != None):
            a.append(current.value)
            current = current.next
        print(a)

# CREATE NEW
lk1 = linkedList()

# ADD LAST
lk1.addLast(10)
lk1.addLast(20)
lk1.addLast(30)

# ADD FIRST
# lk1.addFirst(40)

# INDEX OF
# print(lk1.indexOf(20))

# CONTAINS
# print(lk1.contains(20))

# REMOVE FIRST
# lk1.removeFirst()

# REMOVE FIRST
# lk1.removeLast()

# PRINT
# lk1.print()

# SIZE
# print(lk1.size())

# TO ARRAY
# lk1.toArray()