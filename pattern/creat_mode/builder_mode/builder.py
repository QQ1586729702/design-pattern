from abc import ABC, abstractmethod
from computer import Computer


class Builder(ABC):
    computer = Computer()

    @abstractmethod
    def create_cpu(self) -> Computer.cpu:
        pass

    @abstractmethod
    def create_main_bord(self) -> Computer.main_bord:
        pass

    @abstractmethod
    def create_graphics_card(self) -> Computer.graphics_card:
        pass

    def create_computer(self) -> Computer:
        return self.computer


class HPBuilder(Builder):
    def create_cpu(self) -> Computer.cpu:
        self.computer.cpu = "HPCpu"
        return self.computer.cpu

    def create_main_bord(self) -> Computer.main_bord:
        self.computer.main_bord = "HPMainBord"
        return self.computer.main_bord

    def create_graphics_card(self) -> Computer.graphics_card:
        self.computer.graphics_card = "HPGraphicsCard"
        return self.computer.graphics_card


class LXBuilder(Builder):
    def create_cpu(self) -> Computer.cpu:
        self.computer.cpu = "LXCpu"
        return self.computer.cpu

    def create_main_bord(self) -> Computer.main_bord:
        self.computer.main_bord = "LXMainBord"
        return self.computer.main_bord

    def create_graphics_card(self) -> Computer.graphics_card:
        self.computer.graphics_card = "LXGraphicsCard"
        return self.computer.graphics_card
