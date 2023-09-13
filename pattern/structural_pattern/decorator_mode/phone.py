from abc import ABC, abstractmethod


# 抽象手机类
class Phone(ABC):
    name: str
    space_size: float

    @abstractmethod
    def get_phone_description(self) -> str:
        pass

    @abstractmethod
    def get_residual_size(self) -> float:
        pass


# 具体一加手机类
class OnePlusPhone(Phone):
    name = "一加手机"
    space_size = 256 * 1024

    def get_phone_description(self) -> str:
        return self.name

    def get_residual_size(self) -> float:
        return self.space_size


# 具体苹果手机类
class ApplePhone(Phone):
    name = "苹果手机"
    space_size = 128 * 1024

    def get_phone_description(self) -> str:
        return self.name

    def get_residual_size(self) -> float:
        return self.space_size
