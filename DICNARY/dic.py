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


# thisdict: dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020 # this will overwrite the previous key:vlaue
# }
# print(thisdict)


# print("person.items()        = ", person.items()) 



# you can't unpack the value in dic
# key,val = {"name": "zaid"}
# print(key)


# you can theese method
# k={"name": "zaid"}.items().__iter__().__next__()
# print(k)


# and also this 
# ob = {"name": "mhamikl","class": "second year"}
# for k,v in ob.items():
#     print(k +":" + v)




sentence = """
**Projected Economy Size of AI:**

The projected economy size of AI is significant, with estimates varying depending on the source and methodology. Here are some notable projections:

1. **Global AI Market Size:**
	* By 2025: 
1.5 trillion (Source: PwC)
2. **AI-Driven Economic Growth:**
	* By 2025: AI is expected to contribute 10% to global GDP growth (Source: Accenture)
	* By 2030: AI is expected to contribute 14% to global GDP growth (Source: PwC)
3. **AI-Generated Revenue:**
	* By 2025: AI is expected to generate 
33.5 trillion in revenue (Source: McKinsey)
4. **Job Market Impact:**
	* By 2025: AI is expected to create 133 million new jobs globally (Source: World Economic Forum)
	* By 2030: AI is expected to automate 30% of current jobs globally (Source: McKinsey)

**Industry-Specific Projections:**

1. **Healthcare:**
	* By 2025: AI is expected to generate 
100 billion in revenue (Source: Accenture)
3. **Manufacturing:**
	* By 2025: AI is expected to generate 
20 billion in revenue (Source: MarketsandMarkets)

**Regional Projections:**

1. **North America:**
	* By 2025: AI is expected to generate 
50 billion in revenue (Source: IDC)
3. **Asia-Pacific:**
	* By 2025: AI is expected to generate $200 billion in revenue (Source: MarketsandMarkets)

Note: These projections are based on various assumptions, including the pace of AI development, adoption rates, and economic trends. The actual economy size of AI may vary depending on several factors.

"""
     


# words_count = {}

# for c in sentence.split():
#     if c in words_count:
#         words_count[c] +=1
#     else:
#         words_count[c]=1

# # print(words_count)

# sortedWord = dict(sorted(words_count.items(),key=lambda item:item[1]))
# print(sortedWord)




