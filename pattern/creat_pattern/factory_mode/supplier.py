from factory import ProduceFactory


class Supplier:
    def __init__(self, factory: ProduceFactory):
        self._factory = factory
        self._phone = self._factory.create_phone()
        self._computer = self._factory.create_computer()

    def sell_computer_product(self):
        print("卖出" + self._computer.get_name())

    def sell_phone_product(self):
        print("卖出" + self._phone.get_name())
