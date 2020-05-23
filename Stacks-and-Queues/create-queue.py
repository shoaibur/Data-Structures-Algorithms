class Queue(object):
    def __init__(self):
        self.queue = []
    
    def enq(self, value):
        self.queue.insert(0,value)
      
    def deq(self):
        self.queue.pop()
# Create a queue
q = Queue()
q.enq(1)
q.enq(2)
q.enq(3)
print(q.queue) # [3, 2, 1]
q.deq()
print(q.queue) # [3, 2]
