from abc import abstractmethod, ABC


class AbstractSkin(ABC):
    @abstractmethod
    def display(self):
        pass
    