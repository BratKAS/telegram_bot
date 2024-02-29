from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


person_info: Person = {'name': 'Alice', 'age': 30}
print(person_info)
