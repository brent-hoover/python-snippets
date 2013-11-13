import Queue, heapq, time
class PriorityQueue(Queue.Queue):
    # Initialize the queue
    def _init(self, maxsize):
        self.maxsize = maxsize
        self.queue = []
    # Return the number of items that are currently enqueued
    def _qsize(self):
        return len(self.queue)
    # Check whether the queue is empty
    def _empty(self):
        return not self.queue
    # Check whether the queue is full
    def _full(self):
        return self.maxsize > 0 and len(self.queue) >= self.maxsize
    # Put a new item in the queue
    def _put(self, item):
        heapq.heappush(self.queue, item)
    # Get an item from the queue
    def _get(self):
        return heapq.heappop(self.queue)
    # shadow and wrap Queue.Queue's own `put' to allow a 'priority' argument
    def put(self, item, priority=0, block=True, timeout=None):
        decorated_item = priority, time.time(), item
        Queue.Queue.put(self, decorated_item, block, timeout)
    # shadow and wrap Queue.Queue's own `get' to strip auxiliary aspects
    def get(self, block=True, timeout=None):
        priority, time_posted, item = Queue.Queue.get(self, block, timeout)
        return item
