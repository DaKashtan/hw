class List:
    def __init__(self):
        self.list = []
    def add(self,obj):
        self.list.append(obj)

    def delete(self,obj):
        self.list.remove(obj)

    def insert(self,obj,ind):
        self.list.insert(ind,obj)
    def length(self):
        return len(self.list)
    def find(self,ind):
        return self.list[ind]

class Queue:

    def __init__(self):
        self.queue = []

    def push(self, obj):
        self.queue.insert(0,obj)

    def pull(self):
        ind=len(self.queue)
        self.queue.pop(ind-1)
    def length(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, obj):
        self.stack.append(obj)

    def pull(self):
        ind=len(self.stack)
        self.stack.pop(ind-1)
    def length(self):
        return len(self.stack)