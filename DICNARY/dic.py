# Create a dictionary to store a person's details
person: dict = {
    "name": "Alice",
    "age": 25,
    "visited_cities": "amerca"
}
# print(person)

# print(person["class"] )   erutrn ke yerror 
# but you acess the key it will not gives error the syntax is givEN below 
# print(person.get("class", "eoght"))





# 5. Deleting Items
# You can remove a key-value pair using the del keyword or the pop() method.

# Note that pop() returns the value of the removed key-value pair, whereas del does not return anything.

# You can also use pop() with a default value, in case the key is not found in the dictionary:

# Example Code:

person: dict = {'name': 'Alice', 'age': 25, 'email': 'alice@example.com', 'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
# print(person)

# with del method
# del person["name"]
# print(person)


# delete pop() method 


# isMarried= person.pop("isMarried")
# print(isMarried)



#  Dictionary Methods
  
# we have several mthodd of dictaionatr   but we will cober  some important method


# Method	Description	

# keys()	Returns a list of all keys in the dictionary.	
# values()	Returns a list of all values in the dictionary.	
# items()	Returns a list of key-value pairs as tuples.	
# clear()	Removes all items from the dictionary.	
# update()	Adds or updates multiple key-value pairs from another dictionary.	


# print(person.values())
# print(person.keys())

# person.update({"name": "mohamil" , "age" :19
# })
# print(person)


thisdict: dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 # this will overwrite the previous key:vlaue
}
print(thisdict)