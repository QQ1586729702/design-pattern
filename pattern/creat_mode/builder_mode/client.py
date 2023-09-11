from class_builder import Builder
from director import Directory
from builder import HPBuilder

if __name__ == '__main__':
    # 第一种Builder
    directory = Directory(HPBuilder())
    computer1 = directory.construct()
    print(computer1.cpu)
    print(computer1.main_bord)
    print(computer1.graphics_card)

    # 第二种Builder
    computer = Builder()\
        .builder_cpu("LXCpu")\
        .builder_main_bord("LXMainBord")\
        .builder_graphics_card("LXGraphicsCard")\
        .builder()
    print(computer.cpu)
    print(computer.graphics_card)
    print(computer.main_bord)
