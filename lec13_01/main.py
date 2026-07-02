from threading import Thread
from time import sleep
import timeit

# change me vv
num_threads = 4
# change me ^^

# Divide work units by the number of threads
work_units = 12
units_per_thread = work_units // num_threads
# Check that work units are divisible by number of threads
if units_per_thread * num_threads != work_units:
	print("12 must be divisible by num_threads")
	exit()


# Thread body
def thread_body(thread_id):
	for i in range(units_per_thread):
		# Pretend to do something slow, like wait for a network connection
		#  or read from disk
		sleep(1)


# Launch threads which perform the work
def do_work():
	print("Launching threads...")
	ts = []
	for i in range(num_threads):
		t = Thread(target=thread_body, args=(i, ))
		t.start()
		ts.append(t)

	print("Waiting...")
	for t in ts:
		t.join()

	print("All threads finished!")


print("Time:", int(timeit.timeit(do_work, number=1)))
