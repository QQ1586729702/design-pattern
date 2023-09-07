from abc import ABC, abstractmethod


class Phone(ABC):
    @abstractmethod
    def get_name(self):
        pass


class OnePlusPhone(Phone):
    def get_name(self) -> str:
        return "一加手机"


class ApplePhone(Phone):
    def get_name(self):
        return "苹果手机"
