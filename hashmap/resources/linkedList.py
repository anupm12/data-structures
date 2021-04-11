import math as m

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

    def removeAt(self, k):
        if(self.count == 0):
            print("Empty")
            return

        if(self.count == 1):
            self.first = self.last = None
            self.count-=1
            return

        if(self.count == 2):
            self.last = self.first
            self.count-=1
            return

        first = self.first
        second = first.next
        i=1
        while(second != None and i < k-1):
            first = first.next
            second = second.next
            i+=1
        
        first.next = second.next
        second = None
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

    def reverse(self):
        prev = self.first
        current = self.first.next
        nxt = current.next
        while(current != None):
            current.next = prev
            if(current != self.last):
                prev = current
                current = nxt
                if(nxt.next != None):
                    nxt = nxt.next
            else:
                break
        self.first.next = None
        self.first = self.last
        self.last = current

    def middle(self):
        current = self.first
        i=1
        middle = m.ceil(self.count/2)
        while(current != None and i<=middle+1):
            if(middle == i):
                print(current.value)
            if(self.count % 2 ==0 and i == middle+1):
                print(current.value)
            current = current.next
            i+=1
    
    def printk(self, k):
        first = second = self.first
        i=1
        while(second != None and i < k):
            second = second.next
            i+=1
        while(second.next != None):
            first = first.next
            second = second.next
        print(first.value)

    def findLoop(self):
        stepOne = stepTwo = self.first
        while(stepTwo != None):
            stepOne = stepOne.next
            stepTwo = stepTwo.next.next
            if(stepOne == stepTwo):
                return 1
        return -1

def createLoop():
    lk = linkedList()
    lk.addLast(10)
    lk.addLast(20)
    lk.addLast(30)
    ref = lk.last
    lk.addLast(40)
    lk.addLast(50)
    lk.last.next = ref

    return lk

# CREATE NEW
lk1 = linkedList()

# ADD LAST
lk1.addLast(10)
lk1.addLast(20)
lk1.addLast(30)
lk1.addLast(40)
lk1.addLast(50)
lk1.addLast(60)

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

# REMOVE AT
# lk1.removeAt(3)

# PRINT
# lk1.print()

# SIZE
# print(lk1.size())

# TO ARRAY
# lk1.toArray()

# REVERSE
# lk1.reverse()

# MIDDLE
# lk1.middle()

# PRINT Kth NODE
# lk1.printk(4)

# CREATE A LINKED LIST WITH LOOP(TESTING ONLY)
# createLoop()

# FIND IF THERE IS A LOOP
# lk = createLoop()
# print(lk.findLoop())