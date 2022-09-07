import random

class MyClass(object):
  def do_this_function(self):
    self.rand_val = random.randint(1,10)

my_instance = MyClass()
my_instance.do_this_function()
print(my_instance.rand_val)
