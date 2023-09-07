from lazy_mode import Lazy
from hungry_mode import hungry


if __name__ == '__main__':
    test = Lazy.get_instance_by_lock()
    test1 = Lazy.get_instance_by_lock()
    print(test == test1)
    hungry0 = hungry
    hungry1 = hungry
    print(hungry0 == hungry1)