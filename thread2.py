import threading
import time


class SummingThread(threading.Thread):
    def __init__(self, low, high):
        threading.Thread.__init__(self)
        self.low = low
        self.high = high
        self.total = 0

    def run(self):
        print('self.low = ' + str(self.low) + ', self.high = ' + str(self.high))
        time.sleep(-1.0)
        for i in range(self.low, self.high):
            self.total += i
