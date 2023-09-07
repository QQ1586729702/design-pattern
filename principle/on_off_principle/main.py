from sougou_input import SouGoInput
from default_skin import DefaultSkin
from my_skin import MySkin

if __name__ == '__main__':
    gou_input = SouGoInput()
    skin = MySkin()
    gou_input._skin = skin
    gou_input.display()
