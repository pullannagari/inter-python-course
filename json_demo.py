# comes with built in json module
import json
from typing import Any

# python dictionary to json object
person = {"name": "john", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
personJson = json.dumps(person, indent = 4, sort_keys=True)
print(personJson)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# json to python dictionary
with open("person.json", "r") as file:
    person = json.load(file)
    print(person)


class User:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

user = User("Max", 27)
# userJson = json.dumps(user) # gives a TypeError: Object of type User is not JSON serializable

# write a custom encoding function
def encode_user(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError('TypeError: Object of type User is not JSON serializable')

userJson = json.dumps(user, default=encode_user)
print(userJson)

# we can also implement a custom encoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, User):
            return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
        return super().default(o)
    
userJson = UserEncoder().encode(user)
print(userJson)

# decoding the object
user = json.loads(userJson)
print(user) # this is a dict
# print(user.name) AttributeError: 'dict' object has no attribute 'name'

# need to write a custom decoding method
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])

user = json.loads(userJson, object_hook=decode_user)
print(user.name)