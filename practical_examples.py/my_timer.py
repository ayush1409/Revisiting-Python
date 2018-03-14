
import time

def my_timer(original_func):

	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = original_func(*args,**kwargs)
		t2 = time.time() - t1

		print('{} ran for {} secs'.format(original_func.__name__, t2))

	return wrapper

@my_timer
def display_info(name, age):
	time.sleep(1)
	print('hello {0} {1}'.format(name, age))

display_info('michael', 21)
