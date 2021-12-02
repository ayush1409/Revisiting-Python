# Common problems that we can encounter when using default parameter.
from datetime import datetime
import time


def fun(a=10):  # this statement is compiled completely
    # if we don't pass the any value to a, it will point to 10 always
    print(a)    # now a pointing to a immutable(int) 10


# logger function
def log_msg(message, log_time=datetime.utcnow()):
    print(message, log_time)


# Note: both messages are logged using the same timestamp
log_msg('message 1')
time.sleep(2)
log_msg('message 2')


# solution to the above problem
def log_msg2(message, log_time=None):
    # If no time passed, log using the current time
    log_time = log_time or datetime.utcnow()
    print(message, log_time)


log_msg2('message 1')
time.sleep(2)
log_msg2('message 2')


# Note: instead of None, if we assign a mutable object such as list then its value may change
# and produce different result based on the current value of that list




