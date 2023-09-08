from abc import ABC, abstractmethod


class Cloneable(ABC):
    @abstractmethod
    def deep_clone(self):
        # 抽象类深克隆方法
        pass

    @abstractmethod
    def shallow_clone(self):
        # 抽象类浅克隆方法
        pass



