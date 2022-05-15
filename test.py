# `abc` module provides a facility for creating abstract classes.
# These are classes that are not designed to be instantiated but only to be sub classed.
# We don't create a `GetterSetter` instance. We only inherit from it.
import abc

# We don't create a `GetterSetter` instance. We only inherit from it.
class GetterSetter(object):
  # Create an abstract base class is to use a `__metaclass__`.
  # `__metaclass__` is a class that can define other classes.
  __metaclass__ = abc.ABCMeta

  # Place a decorator to indicate that these methods are abstract methods.
  @abc.abstractmethod
  def set_val(self, input):
    """Set a value in the instance."""
    return

  @abc.abstractmethod
  def get_val(self):
    "Get and return a value from the instance."""
    return

# Create a subclass of `GetterSetter`
class MyClass(GetterSetter):

  # Fullfill the contract for `set_val` method with the Abstract parent class.
  def set_val(self, input):
    self.val = input

  # Fullfill the contract for `set_val` method with the Abstract parent class.
  def get_val(self):
    return self.val

x = MyClass()
print(x)
