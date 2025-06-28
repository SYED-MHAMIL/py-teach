# Set is one of `4 built-in data types` in Python used to store collections of data, the other 3 are **`List, Tuple, and Dictionary`**, all with different qualities and usage.

# A set is:
#   - **unordered**
#   - **unindexed**
#   - **mutable**


# my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
# print("my_set = ", my_set)

# # discard() only removes a single element.
# # {1, 2, 3} is a set itself, not an element within my_set.
# # Therefore, discard does not find it and returns None, without modifying the set.
# print(my_set.discard({1,2,3}))

# print("After: my_set = ", my_set) # return None

# # To remove multiple elements, iterate and discard each one individually:
# for item in {1, 2, 3}:
#     my_set.discard(item)

# print("After removing multiple elements: my_set = ", my_set)






# a = 'abc'
# b = 'xyz'


# hash(a) % 8 == 4
# hash(b) % 8 == 4

# Now both want to go into slot 4 → that's a collision.
