from stack import stack

class queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.front = 0
        self.rear = 0
        self.count = 0
    
    def print(self):
        temp = self.front
        for i in range(self.count):
            print(self.queue[temp])
            temp+=1
            temp = temp % self.size
    
    def enqueue(self, value):
        if(self.count == len(self.queue)):
            return -1
        else:
            self.queue[self.rear % self.size] = value
            self.rear+=1
            self.count+=1
            return 1
    
    def dequeue(self):
        if(self.count == 0):
            return -1
        else:
            val = self.queue[self.front % self.size]
            self.queue[self.front % self.size] = None
            self.front+=1
            self.count-=1
            return val

    def reverse(self):
        stk = stack(self.size)
        temp = self.front
        for i in range(self.count):
            stk.push(self.queue[temp])
            temp+=1
            temp = temp % self.size
        while(not stk.isEmpty()):
            print(stk.pop())

def reverseK(k, que):
    stk = stack(que.size)
    q = queue(que.size)
    for i in range(k):
        stk.push(que.dequeue())
    for i in range(que.count+k):
        if(not stk.isEmpty()):
            q.enqueue(stk.pop())
        else:
            q.enqueue(que.dequeue())
    q.print()

# que = queue(5)

#ENQUEUE
# que.enqueue(1)
# que.enqueue(2)
# que.enqueue(3)
# que.print()

# DEQUEUE
# que.dequeue()
# que.dequeue()
# que.dequeue()
# que.enqueue(1)
# que.enqueue(2)
# que.enqueue(3)
# que.print()

# REVERSE
# que.reverse()

#REVERSE UPTO K
# reverseK(2, que)

