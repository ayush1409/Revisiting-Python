# Monkey patching by decorating classes
# Monkey patching is basically adding additional attributes in classes,
# The classes may be standard library class or user defined classes

from fractions import Fraction

# basic idea
Fraction.is_integral = lambda self: self.denominator == 1
f1 = Fraction(2, 3)
f2 = Fraction(4, 1)

print(f1.is_integral())     # False
print(f2.is_integral())     # True

def dec_speak(cls):
    cls.speak = lambda self, message: "{0} says {1}".format(self.__class__.__name__,
                                                            message)
    return cls
# Note: we are actually mutating the class, so there is no need to return it,
# we are returning class just to be consistent with the decorator syntax

# adding speak functionality in Fraction class
Fraction = dec_speak(Fraction)
print(f1.speak("It works!"))    # Fraction says It works!

class Person:
    pass

# adding speak functionality in Person class
Person = dec_speak(Person)
p = Person()
print(p.speak("Hello!"))    # Person says Hello!

# Application of monkey patching: adding debug info by mutating the class
from datetime import datetime, timezone
def info(self):
    result = list()
    result.append('time: {0}'.format(datetime.now(timezone.utc)))
    result.append('Class : {0}'.format(self.__class__.__name__))
    result.append('id: {0}'.format(hex(id(self))))
    for k, v in vars(self).items():
        result.append('{0}: {1}'.format(k, v))
    return result

def debug_info(cls):
    cls.debug = info
    return cls  # Return only when we need to use decorator syntax i.e. @

@debug_info
class Person:
    def __init__(self, a, b):
        self.a = a
        self.b = b

p = Person(10, 20)
print(p.debug())
# ['time: 2021-07-09 16:48:24.421839+00:00', 'Class : Person', 'id: 0x8a4820', 'a: 10', 'b: 20']