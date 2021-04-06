class queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.count = 0
        self.front = 0
        self.rear = 0
    
    def print(self):
        temp = self.front
        for i in range(self.count):
            print(self.queue[temp])
            temp+=1
            temp = temp % self.size

    def enqueue(self, val):
        if(self.count == self.size):
            print("Queue full")
            return
        elif(self.count == 0):
            self.queue[self.rear%self.size] =  val
            self.rear+=1
            self.count+=1
            return
        else:
            pos = self.rear
            for i in range(self.count):
                if(val < self.queue[pos-1]):
                    self.queue[pos%self.size] = self.queue[pos-1]
                    self.queue[pos-1] = val
                else:
                    self.queue[pos%self.size] = val
                    break
                pos-=1
                pos = pos % self.size
            self.rear+=1
            self.count+=1

    def dequeue(self):
        if(self.count == 0):
            print("Queue empty")
            return
        else:
            self.queue[self.rear - 1 % self.size] = None
            self.rear-=1
            self.count-=1

# que = queue(5)

# que.enqueue(10)
# que.enqueue(5)
# que.enqueue(4)
# que.enqueue(6)
# que.enqueue(18)

# que.dequeue()

# que.print()
