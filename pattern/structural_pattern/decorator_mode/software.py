from phone import Phone
from abc import ABC


class Software(Phone, ABC):
    def __init__(self, phone: Phone):
        self.phone = phone


class AppStore(Software):
    name = "应用商店"
    space_size = 10

    def get_phone_description(self) -> str:
        return self.phone.get_phone_description() + "安装了" + self.name

    def get_residual_size(self) -> float:
        return self.phone.get_residual_size() - self.space_size


class QQ(Software):
    name = "QQ"
    space_size = 100

    def get_phone_description(self) -> str:
        return self.phone.get_phone_description() + "安装了" + self.name

    def get_residual_size(self) -> float:
        return self.phone.get_residual_size() - self.space_size
    