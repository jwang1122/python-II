from student import *
import json

json_string = """{
    "first_name": "John",
    "last_name": "Wang",
    "id": "12345",
    "gender": "male",
    "age": 13
}"""

s1 = student_from_dict(json.loads(json_string))
print(type(s1))
print(s1.first_name)
print(s1.last_name)
print(s1)