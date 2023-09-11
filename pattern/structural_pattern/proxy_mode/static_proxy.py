from abc import ABC, abstractmethod


class SellComputer(ABC):
    @abstractmethod
    def sell(self):
        pass


class Producer(SellComputer):
    _price = 10

    def sell(self):
        print("生产商卖出了电脑")

    @property
    def price(self):
        return self._price


class Supplier(SellComputer):
    _producer = Producer()
    name: str
    price: int

    def sell(self):
        print(f'{self.name}卖出了电脑,并且赚取了差价{self.price - self._producer.price}')
        self._producer.sell()


class ChinaSupplier(Supplier):
    name = '中国供应商'
    price = 20


class AmericaSupplier(Supplier):
    name = '美国供应商'
    price = 30


if __name__ == '__main__':
    supplier = ChinaSupplier()
    supplier.sell()
