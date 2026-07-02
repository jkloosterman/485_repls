from threading import Thread
from threading import Lock

num_threads = 3
num_increments = 1000000

# Shared variable
x = 0

# Thread body
def thread_body():
  global x
  for i in range(num_increments):
    # Hint: x += 1 does multiple things. What are they?
    #  What would happen if the OS decided to switch threads
    #  on the CPU between them?
    x += 1

# Launch threads
ts = []
for i in range(num_threads):
  t = Thread(target=thread_body)
  t.start()
  ts.append(t)

# Wait for all threads to exit
for t in ts:
  t.join()

print("x:", x, "Expected:", num_threads * num_increments)
