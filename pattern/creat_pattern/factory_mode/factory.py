from abc import ABC, abstractmethod
from computer import OnePlusComputer, AppleComputer, Computer
from phone import ApplePhone, OnePlusPhone, Phone


class ProduceFactory(ABC):
    @abstractmethod
    def create_phone(self) -> Phone:
        pass

    @abstractmethod
    def create_computer(self) -> Computer:
        pass


class OnePlusFactory(ProduceFactory):
    def create_phone(self) -> Phone:
        return OnePlusPhone()

    def create_computer(self) -> Computer:
        return OnePlusComputer()


class AppleFactory(ProduceFactory):
    def create_computer(self) -> Computer:
        return AppleComputer()

    def create_phone(self) -> Phone:
        return ApplePhone()
