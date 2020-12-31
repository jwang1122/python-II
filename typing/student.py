# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = student_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Student:
    first_name: str
    last_name: str
    id: int
    gender: str
    age: int

    def __init__(self, first_name: str, last_name: str, id: int, gender: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.gender = gender
        self.age = age

    @staticmethod
    def from_dict(obj: Any) -> 'Student':
        assert isinstance(obj, dict)
        first_name = from_str(obj.get("first_name"))
        last_name = from_str(obj.get("last_name"))
        id = int(from_str(obj.get("id")))
        gender = from_str(obj.get("gender"))
        age = from_int(obj.get("age"))
        return Student(first_name, last_name, id, gender, age)

    def to_dict(self) -> dict:
        result: dict = {}
        result["first_name"] = from_str(self.first_name)
        result["last_name"] = from_str(self.last_name)
        result["id"] = from_str(str(self.id))
        result["gender"] = from_str(self.gender)
        result["age"] = from_int(self.age)
        return result

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"

def student_from_dict(s: Any) -> Student:
    return Student.from_dict(s)


def student_to_dict(x: Student) -> Any:
    return to_class(Student, x)
