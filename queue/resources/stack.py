class stack:
    def __init__(self, size):
        self.size = size
        self.stk = [None] * self.size
        self.top = 0
    
    def print(self):
        for i in range(self.top):
            print(self.stk[i])

    def isEmpty(self):
        return self.top == 0

    def push(self, value):
        if(self.top == self.size):
            print("Stack full")
            return
        if(self.top < self.size):
            self.stk[self.top] = value
            self.top+=1

    def pop(self):
        if(self.isEmpty()):
            print("Stack empty")
        else:
            self.top-=1
            return self.stk[self.top]

    def peek(self):
        if(self.isEmpty()):
            print("Stack empty")
        else:
            return self.stk[self.top-1]
    
    def reverse(self):
        if(self.isEmpty()):
            print("Stack empty")
        else:
            for i in self.stk[self.top-1::-1]:
                print(i)

    def balEqn(self, eqn):
        open = ['[', '{', '<', '(']
        close = [']', '}', '>', ')']
        for val in eqn:
            if(val in open):
                self.push(val)
            elif(not stk.isEmpty()):
                if(val in close and close.index(val) == open.index(stk.peek())):
                    self.pop()
                else:
                    return -1
            else:
                return -1
        return 1
    
        

stk = stack(5)

# stk.push(10)
# stk.push(20)
# stk.push(30)
# stk.push(40)

# PRINT
# stk.print()

# POP
# stk.print()
# stk.pop()
# stk.print()

# PEEK
# stk.peek()

# REVERSE
# stk.reverse()

# BALANCED EQUATION
print(stk.balEqn(" "))