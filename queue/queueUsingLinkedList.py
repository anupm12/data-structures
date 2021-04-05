from resources.linkedList import linkedList

lk = linkedList()

class queue:

    def enqueue(self, val):
        lk.addLast(val)

    def dequeue(self):
        lk.removeFirst()

    def peek(self):
        print(lk.first.value)

    def size(self):
        print(lk.count)

    def isEmpty(self):
        print(lk.isEmpty())

que = queue()

que.enqueue(10)
que.enqueue(20)
que.enqueue(30)

# que.dequeue()

# lk.print()

# que.peek()

# que.size()

# que.isEmpty()

