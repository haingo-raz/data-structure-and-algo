from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t) # Add the new request time to the queue

        while t - self.q[0] > 3000:
            self.q.popleft() # Remove old request

        return len(self.q)
    