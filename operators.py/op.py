class Person:
    def __init__(self, name):
        self._name = name  # internal use only

p = Person("Alice")
print(p._name)  # This works, but it's discouraged


