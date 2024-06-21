class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0

    def enqueue(self, item):
        if self.num >= self.max_size:
            raise Exception("queue is full")
        self.Q[(self.first + self.num)% self.max_size] = item
        self.num += 1

    def dequeue(self):
        if self.num == 0:
            raise Exception("queue is empty")
        item = self.Q[self.first]
        self.first = (self.first + 1) % self.max_size
        self.num -= 1
        return item

    def front(self):
        if self.num == 0:
            raise Exception("queue is empty")
        return self.Q[self.first]

    def is_empty(self):
        return self.num == 0

    def is_full(self):
        return self.num >= self.max_size

    def size(self):
        return self.num

    def asked_object(self, index):
        if self.num == 0:
            raise Exception("queue is empty")
        item = self.Q[index]
        if index == self.first:
            self.first = (self.first + 1) % self.max_size
        self.num -= 1
        return item