import random

class Animal(object):
  def __init__(self, name):
    self.name = name

class Dog(Animal):

  # Now 'Dog' has it's own `__init__`.
  def __init__(self, name):
    # `super` is a buil-in function designed to relate a class to it's `super class` (parent class).
    # `super` says: get the `super` class of `Dog` and pass the `Dog` instance to whatsever method we state here (here's `__init__` now).
    # We are calling `Animal.__init__` with 'Dog' object
    # `super` alows to keep things modular.
    # Allows to separate common functionality from more specific functionality.
    # We could write instead:
    # Animal.__init__(name)
    Animal.__init__(self, name)
    self.breed = random.choice(['Shiu Tzu', 'Beagle', 'Mutt'])

  def fetch(self, thing):
    print ('%s goes after the %s' % (self.name, thing))

d = Dog('dogname')

print(d.name)
print(d.breed)
