import json
from typing import NamedTuple

_j = '{"name":"Robert","age":37,"mother":{"name":"Anna","age":58},"children":["Barbara","Jasiek","Angelika"],"married": true,' \
     '"dog":null} '


class PersonNameAge(NamedTuple):
    name: str
    age: int


class UserInfo(NamedTuple):
    name: str
    age: int
    mother: PersonNameAge
    children: list
    married: bool
    dog: str


j = json.loads(_j)
u = UserInfo(**j)

print(u.name, u.age, u.mother, u.children, u.married, u.dog)