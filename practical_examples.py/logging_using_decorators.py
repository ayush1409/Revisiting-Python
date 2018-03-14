
def logger(original_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)

	def wrapper(*args, **kwargs):
		logging.info(
			'Running with args "{}" and with kwargs {}'.format(args, kwargs)
		)
		return original_func(*args, **kwargs)
	return wrapper

@logger
def display_info(name, age):
	print('hello {0} {1}'.format(name, age))

display_info('michael', 21)
display_info('chris', 23)
