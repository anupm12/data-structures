from resources.queue import queue

class stack:
    def __init__(self, size):
        self.size = size
        self.q1 = queue(self.size)
        self.q2 = queue(self.size)

    def print(self):
        self.q1.print()

    def push(self, val):
        self.q1.enqueue(val)
    
    def pop(self):
        if(self.q1.count == 0):
            print("Stack empty")        
        else:
            for i in range(self.q1.count-1):
                self.q2.enqueue(self.q1.dequeue())

            self.q1.dequeue()
                    
            for i in range(self.q2.count):
                self.q1.enqueue(self.q2.dequeue())
            
    def peek(self):
        temp = self.q1.front
        for i in range(self.q1.count-1):
            temp+=1
            temp = temp % self.size
        print(self.q1.queue[temp])

    def sizee(self):
        print(self.q1.count)

    def isEmpty(self):
        if(self.q1.count == 0):
            print("True")
        else:
            print("False")

stk = stack(5)

#PUSH
# stk.push(10)
# stk.push(20)

#POP
# stk.pop()
# stk.push(30)

#PRINT
# stk.print()

#PEEK
# stk.peek()

#SIZE
# stk.sizee()

#IS EMPTY
stk.isEmpty()