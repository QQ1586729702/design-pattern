from .earphones import TypeCEarphones


# 一加手机其耳机只支持type-c接口的耳机
class OnePlusPhone:
    def __init__(self, earphones: TypeCEarphones):
        self._earphones = earphones
        self._name = "一加手机"

    def listen(self):
        msg = self._earphones.type_c_listen()
        print(f'{self._name + msg}')

    def talk(self):
        msg = self._earphones.type_c_talk("hello")
        print(f'{self._name + msg}')
