# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# NOTE:
# All the operations have to be constant time operations.
# getMin() should return -1 if the stack is empty.
# pop() should return nothing if the stack is empty.
# top() should return -1 if the stack is empty.
# 1 <= Number of Function calls <= 10^7
class MinStack:
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x):
        self.A.append(x)
        B = self.B
        B.append(x if not B else min(x, B[-1]))

    def pop(self):
        if len(self.A) != 0:
            self.A.pop()
            self.B.pop()

    def top(self):
        if len(self.A) == 0:
            return -1

        return self.A[-1]

    def getMin(self):
        if len(self.A) == 0:
            return -1

        return self.B[-1]


P = MinStack()
P.push(1)
P.push(2)
P.push(-2)
print(P.getMin())
P.pop()
print(P.getMin())
print(P.top())
P.pop()
P.pop()

print(P.getMin())
P.pop()
print(P.top())
