from model.earphones import TypeCEarphones, SonyMovingCoilEarphones, SonyTypeCEarphones, MovingCoilEarphones
from model.phone import OnePlusPhone


# 耳机适配器: type-c头转换圆头 可以适配类以及其子类(圆头的子类,不管什么牌子都可以适配,适配性强)
class EarphonesAdapter(TypeCEarphones):
    def __init__(self, coil_earphones: MovingCoilEarphones):
        self._coil_earphones = coil_earphones

    def type_c_listen(self) -> str:
        return self._coil_earphones.coil_listen()

    def type_c_talk(self, msg: str) -> str:
        return self._coil_earphones.coil_talk(msg)


if __name__ == '__main__':
    phone = OnePlusPhone(SonyTypeCEarphones())
    phone.listen()
    phone.talk()
    print("========================")
    phone = OnePlusPhone(EarphonesAdapter(SonyMovingCoilEarphones()))
    phone.listen()
    phone.talk()
