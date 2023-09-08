from cloneable import Cloneable
from copy import deepcopy, copy


class Student(Cloneable):
    _name: str

    def deep_clone(self) -> 'Student':
        return deepcopy(self)

    def shallow_clone(self) -> 'Student':
        return copy(self)

    def show_name(self):
        print(f'学生名字为:{self._name}')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
