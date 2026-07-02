from threading import Thread
from threading import Lock
import timeit

num_threads = 3
num_increments = 100000

# Shared variable
x = 0
l = Lock()

def acquire_loop_release():
  global x
  l.acquire()
  for i in range(num_increments):
    x += 1
  l.release()  

def acquire_inc_release():
  global x
  for i in range(num_increments):
    l.acquire()
    x += 1
    l.release()

def acquire_inc1000_release():
  global x
  for i in range(num_increments // 1000):
    l.acquire()
    for j in range(1000):
      x += 1
    l.release()    

def launch_threads(body):
  global x
  x = 0

  # Launch threads
  ts = []
  for i in range(num_threads):
    t = Thread(target=body)
    t.start()
    ts.append(t)

  # Wait for all threads to exit
  for t in ts:
    t.join()
  print("x:", x, "Expected:", num_threads * num_increments)

print("acquire_loop_release:", timeit.timeit(lambda: launch_threads(acquire_loop_release), number=1))
print("acquire_inc_release:", timeit.timeit(lambda: launch_threads(acquire_inc_release), number=1))
print("acquire_inc1000_release:", timeit.timeit(lambda: launch_threads(acquire_inc1000_release), number=1))