import json


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Robert", 19)
json = json.dumps(student.__dict__)
print(json)
