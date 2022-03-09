
import time
from thread2 import SummingThread

thread1 = SummingThread(0, 500000)
thread2 = SummingThread(500000, 1000000)

thread1.start()  # This actually causes the thread to run
thread2.start()

thread1.join()  # This waits until the thread has completed
thread2.join()

# At this point, both threads have completed
result = thread1.total + thread2.total
print(result)
