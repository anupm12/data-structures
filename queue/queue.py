from stack import stack

class queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.front = 0
        self.rear = 0
        self.count = 0
    
    def print(self):
        for i in self.queue[:len(self.queue)]:
            print(i)
    
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
            self.queue[self.front % self.size] = None
            self.front+=1
            self.count-=1

    def reverse(self):
        stk = stack(5)
        temp = self.front
        for i in range(self.count):
            stk.push(self.queue[temp])
            temp+=1
            temp = temp % self.size
        while(not stk.isEmpty()):
            stk.pop()

    def reverseK(self, k):
        # for i in range(k):
        #     if(self.queue[i] != None):
        #         print(self.queue[i])
        #     else:
        #         k+=1

que = queue(5)

#ENQUEUE
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
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
que.reverseK(2)