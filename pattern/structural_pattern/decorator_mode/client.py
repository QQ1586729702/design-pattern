from phone import OnePlusPhone, ApplePhone
from software import AppStore, QQ

if __name__ == '__main__':
    phone = OnePlusPhone()
    print(phone.get_phone_description() + "    " + "空间为" + str(phone.get_residual_size()) + "MB")
    phone = AppStore(phone)
    print(phone.get_phone_description() + "    " + "空间为" + str(phone.get_residual_size()) + "MB")
    print("============================================")
    apple_phone = ApplePhone()
    print(apple_phone.get_phone_description() + "    " + "空间为" + str(apple_phone.get_residual_size()) + "MB")
    apple_phone = QQ(apple_phone)
    print(apple_phone.get_phone_description() + "    " + "空间为" + str(apple_phone.get_residual_size()) + "MB")
