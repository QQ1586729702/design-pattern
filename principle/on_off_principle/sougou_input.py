from abstract_skin import AbstractSkin
from dataclasses import dataclass


@dataclass(init=False)
class SouGoInput:
    _skin: AbstractSkin

    def display(self):
        self._skin.display()
