from model.earphones import TypeCEarphones, SonyMovingCoilEarphones, SonyTypeCEarphones
from model.phone import OnePlusPhone


# 耳机适配器: type-c头转换圆头 只能适配索尼圆孔耳机(并非抽象圆孔耳机类,不能适配其他品牌的耳机,适配性差)
class EarphonesAdapter(TypeCEarphones, SonyMovingCoilEarphones):

    def type_c_listen(self) -> str:
        return self.coil_listen()

    def type_c_talk(self, msg: str) -> str:
        return self.coil_talk(msg)


if __name__ == '__main__':
    phone = OnePlusPhone(SonyTypeCEarphones())
    phone.listen()
    phone.talk()
    print("========================")
    phone = OnePlusPhone(EarphonesAdapter())
    phone.listen()
    phone.talk()
