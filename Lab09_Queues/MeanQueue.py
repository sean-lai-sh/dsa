from Lab09_Queues.ArrayQueue import ArrayQueue


class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.sum = 0
    def __len__(self):
        '''Return the number of elements in the queue'''
        return len(self.data)
    def is_empty(self):
        ''' Return True if queue is empty'''
        return self.data.is_empty()
    def enqueue(self, e):
        ''' Add element e to the end of the queue. If e is not an
        int or float, raise a TypeError '''
        if isinstance(e, (int, float)):
            self.data.enqueue(e)
            self.sum += e
    def dequeue(self):
        """ Remove and return the first element from the queue. If
        the queue is empty, raise an exception"""
        if self.is_empty():
            raise Exception("Empty Queue")
        val_return = self.data.dequeue()
        self.sum -= val_return
        return val_return

    def first(self):
        ''' Return a reference to the first element of the queue
    without removing it. If the queue is empty, raise an
    exception '''
        return self.data.first()

    def sum(self):
        return self.sum

    def mean(self):
        return self.sum/len(self)
