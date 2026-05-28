"""Coding Challenge
In order to simply the serialization and deserialization process your task is:
1. Create a function called serialize() that takes 3 arguments: 1) the Python object you want to serialize, 2) the file to which it serializes the object and 3) the serialization protocol which is pickle or json.
The function will create the file (the 2nd argument) and will write the Python object to that file according to its 3rd argument. If the 3rd argument is pickle, It will use pickle to serialize the object and if the argument is json it will use json for serialization.
2. Create a function called deserialize() that takes 2 arguments: 1) the file which contains serialized data and 2) the type of deserialization which is pickle or json.
The function will deserialize from the file into a Python object and will return that object.
3. Test the functions by serializing and deserializing Python objects using both pickle and json.
Note: The script can also be used as a module that will be imported in other Python scripts."""

import pickle
import json

def serialize(obj, file, protocol):
    if protocol == 'pickle':
        with open(file, 'wb') as f:
            pickle.dump(obj, f)

    elif protocol == 'json':
        with open(file, 'w') as f:
            json.dump(obj, f)

    else:
        print("invalid protocol")

def deserialize(file, protocol):
    if protocol == 'pickle':
        with open(file, 'rb') as f:
           return pickle.load(f)

    elif protocol == 'json':
        with open(file, 'r') as f:
            return json.load(f)

    else:
        print("Invalid protocol. Use Pickle or JSON")

# Option 1:

# person = {
#     'name' : 'Dan',
#     'age' : 34,
#     'city' : 'Bucharest'
# }

# nums = [10, 20, 30]

# serialize(person, 'person.pkl', 'pickle')

# data1 = deserialize('person.pkl', 'pickle')
# print(data1)

# serialize(nums, 'nums.json', 'json')

# data2 = deserialize('nums.json', 'json')
# print(data2)

# Option 2:

# if __name__ == "__main__":

"""Important Python concept.
Means:
run this only when file is executed directly
Example:
python script.py
runs.
But if imported:
import script
this block does NOT run.
That is why challenge mentions “can be used as module”."""
 
#     d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')}
 
#     # Serializing using pickle
#     serialize(d1, 'a.dat', 'pickle')
 
#     # Deserializing
#     myDict = deserialize('a.dat', 'pickle')
#     print(f'pickle: {myDict}')
 
#     print('#' * 20)
 
#     # serializing using pickle
#     serialize(d1, 'a.json', 'json')
 
#     # deserializing
#     x = deserialize('a.json', 'json')
#     # Notice how the tuple value was not preserved!
#     print(f'json: {x}')  # {'a': 'x', 'b': 'y', 'c': 'z', '30': [2, 3, 'a']}


"""Why challenge mentions “module”
Because you can save this as: serializer.py
Then another file can import it:
from serializer import serialize, deserialize
serialize(...)
That is what they mean by reusable module."""