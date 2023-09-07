from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


class OnePlusComputer(Computer):
    def get_name(self) -> str:
        return "一加电脑"


class AppleComputer(Computer):
    def get_name(self) -> str:
        return "苹果电脑"
