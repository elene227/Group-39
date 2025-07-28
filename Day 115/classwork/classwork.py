#

person_dictionary = {
    "name": "y/n",
    "age": "y/g",
    "surname": "y/s",
    "academy": "y/a",
    "hobby": "y/h",


}

# dictionary can be changed but there is no duplicates allowed it can be updated indexing is allowed too. it mutable 



info =(person_dictionary.copy())
print(info)

#print(person_dictionary.clear())

print(person_dictionary.get("hobby"))

print(person_dictionary.keys())
print(person_dictionary.items())
print(person_dictionary.values())
print(person_dictionary.pop("academy"))
person_dictionary.update({"hobby": "a"})
print(person_dictionary["hobby"])
print(person_dictionary.popitem())