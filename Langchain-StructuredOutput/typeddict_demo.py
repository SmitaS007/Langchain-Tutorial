from typing import TypedDict
class Person(TypedDict):
    name: str
    age: int    

person1: Person = {"name": "Smita", "age": 33}
print(person1)