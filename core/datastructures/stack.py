"""
    Stack

    A last in first out structure

    Main operations:
        pop()
        push()
        peek()

"""


class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    # remove last inserted item
    def pop(self):
        # get the last data
        data = self.stack[-1]
        del self.stack[-1]

        return data

    # check the last item
    def peek(self, data):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.peek(stack))  # 3
    print(stack.sizeStack())  # 3
    print(stack.pop())  # 3
    print(stack.peek(stack))  # 2
    print(stack.sizeStack())  # 2
