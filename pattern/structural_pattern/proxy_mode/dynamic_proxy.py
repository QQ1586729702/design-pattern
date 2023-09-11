from typing import Callable


class OriginalClass:

    def method(self):
        print("原始类的方法")

    def test(self):
        print("这是测试代码")


class ProxyClass:
    def __init__(self, original):
        self.original = original

    def __getattr__(self, name) -> Callable:
        print("调用了动态代理方法")
        return getattr(self.original, name)

    def __setattr__(self, name, value):
        if name == "original":
            self.__dict__[name] = value
        else:
            setattr(self.original, name, value)


if __name__ == '__main__':
    original_obj = OriginalClass()
    proxy_obj = ProxyClass(original_obj)
    proxy_obj.method()
    proxy_obj.test()