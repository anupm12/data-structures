from resources.linkedList import linkedList

class entry:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value

class hashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def findPos(self, key):
        return key % self.size

    def put(self, key, val):
        pos = self.findPos(key)

        if(self.data[pos] == None):
            self.data[pos] = linkedList()
            self.data[pos].addLast(entry(key, val))
            return
        
        current = self.data[pos].first
        while(current != None):
            if(current.value.key == key):
                current.value.val = val
                return
            current = current.next
        
        self.data[pos].addLast(entry(key, val))
        return

    def get(self, key):
        pos = self.findPos(key)

        if(self.data[pos] != None):
            current = self.data[pos].first
            while(current != None):
                if(current.value.key == key):
                    print(current.value.val)
                    return 
                current = current.next
        print("Not found")

    def remove(self, key):
        pos = self.findPos(key)

        i=1
        if(self.data[pos] != None):
            current = self.data[pos].first
            while(current != None):
                if(current.value.key != key):
                    i+=1
                    current = current.next
                break
        
        self.data[pos].removeAt(i)
        return

ht = hashTable(5)
ht.put(1, 11)
ht.put(2, 22)
ht.put(2, 33)
ht.put(332, 44)
ht.put(555, 55)

# ht.get(22)

# ht.remove(1)