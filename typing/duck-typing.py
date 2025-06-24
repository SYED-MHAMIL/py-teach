
# 🦆 What is Duck Typing?
# Duck typing is a concept from dynamic typing where the type or class of an object is less important than the methods and properties it has.

# 🗣️ "If it walks like a duck and quacks like a duck, it's a duck."

# 🔁 In Python terms:
# If an object can behave like a list (e.g., supports iteration), Python doesn't care whether it's actually a list, tuple, generator, or custom class — as long as it behaves like one.

# ✅ Example:
# python
# Copy
# Edit
# class Duck:
#     def quack(self):
#         print("Quack!")

# class Person:
#     def quack(self):
#         print("I'm pretending to be a duck!")

# def make_it_quack(thing):
#     thing.quack()  # No type checking — only behavior matters

# duck = Duck()
# person = Person()

# make_it_quack(duck)    # Output: Quack!
# make_it_quack(person)  # Output: I'm pretending to be a duck!
# 💡 Python does not care if person is a Duck — it only cares whether it has a quack() method.




# EXAMPLE SECOND 



