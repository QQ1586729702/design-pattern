from supplier import Supplier
from factory import OnePlusFactory, AppleFactory

if __name__ == '__main__':
    factory = AppleFactory()
    supplier = Supplier(factory)
    supplier.sell_phone_product()
    supplier.sell_computer_product()
