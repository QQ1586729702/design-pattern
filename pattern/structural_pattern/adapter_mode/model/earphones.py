from abc import ABC, abstractmethod


# type-c耳机类
class TypeCEarphones(ABC):
    name: str

    @abstractmethod
    def type_c_listen(self) -> str:
        pass

    @abstractmethod
    def type_c_talk(self, msg: str) -> str:
        pass


# 圆孔耳机类
class MovingCoilEarphones(ABC):
    name: str

    @abstractmethod
    def coil_listen(self) -> str:
        pass

    @abstractmethod
    def coil_talk(self, msg: str) -> str:
        pass


# 索尼type-c耳机类
class SonyTypeCEarphones(TypeCEarphones):
    name = "索尼type-c耳机"

    def type_c_listen(self) -> str:
        return f'使用{self.name}听歌'

    def type_c_talk(self, msg: str) -> str:
        return f'使用{self.name}讲话:{msg}'


# 索尼圆孔耳机类
class SonyMovingCoilEarphones(MovingCoilEarphones):
    name = "索尼圆孔耳机"

    def coil_listen(self) -> str:
        return f'使用{self.name}听歌'

    def coil_talk(self, msg: str) -> str:
        return f'使用{self.name}讲话:{msg}'
