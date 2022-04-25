class C:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __hash__(self):
        return hash(self.age)

    def __bool__(self):
        return self.age > 0

alice = C(15)
bob = C(30)
rel = 'younger' if alice < bob else 'older'
print(f'Alice is {rel} than Bob')
print(hash(alice))
