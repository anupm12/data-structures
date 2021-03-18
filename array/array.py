class array:
    def __init__(self,size):
        self.arr = [None] * size
        self.count=0
    
    def print(self):
        for i in self.arr[:self.count]:
            print(i)
    
    def insert(self,val):
        if(self.count == len(self.arr)):
            tmp = [None] * (len(self.arr)*2)

            for i in range(self.count):
                tmp[i] = self.arr[i]
            
            self.arr = tmp

        self.arr[self.count] = val
        self.count+=1

    def removeAt(self,index):
        if(index>=0 and index<self.count-1):
            for i in range(index,self.count-1):
                self.arr[i] = self.arr[i+1]
            self.count-=1
        else:
            return -1

    def indexOf(self,value):
        for i in range(self.count):
            if(self.arr[i] == value):
                return i
        return -1

    def max(self):
        m=self.arr[0]
        for i in range(self.count):
            if(self.arr[i]>m):
                m=self.arr[i]
        return m

    def intersect(self, arr2): 
        a= []       
        for i in range(arr1.count):
            for j in range(arr2.count):
                if(arr1.arr[i] == arr2.arr[j]):
                    a.append(arr1.arr[i])
        return a
    
    def reverse(self):
        tmpArray = [None] * self.count
        j=self.count-1
        for i in range(self.count):
            tmpArray[i] = self.arr[j]
            j-=1
        self.arr = tmpArray

    def insertAt(self,value, index):
        if(self.count == len(self.arr)):
            tmp = [None] * (len(self.arr)*2)
            for i in range(self.count):
                tmp[i] = self.arr[i]
            self.arr = tmp

        for i in reversed(range(self.count+1)):
            if(i>index+2):
                self.arr[i] = self.arr[i-1]

        self.arr[index] = value

# CREATE ARRAY
arr1 = array(4)

# INSERT
arr1.insert(1)
arr1.insert(2)
arr1.insert(3)
arr1.insert(4)

# REMOVE AT
# print(arr1.removeAt(6))
# arr1.print()

# INDEX OF
# print(arr1.indexOf(6))

# MAX
# print(arr1.max())

# CREATE ARRAY
# arr2 = array(2)
# arr2.insert(1)
# arr2.insert(5)
# arr2.insert(9)

# INTERSECT
# print(arr1.intersect(arr2))

# REVERSE
# arr1.reverse()
# arr1.print()

# INSERT AT
# arr1.insertAt(20, 1)
# arr1.print()
