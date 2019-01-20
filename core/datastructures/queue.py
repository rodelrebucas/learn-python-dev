"""
    Stack

    A first in first out structure  

    Main operations:
        enqueue
        dequeue

"""


class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]

        return data

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.peek())  # 1
    print(queue.sizeQueue())  # 3
    print(queue.dequeue())  # 1
    print(queue.peek())  # 2
    print(queue.sizeQueue())  # 2
