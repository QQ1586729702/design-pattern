
# 使用builder类创建类
class ComputerBuilder:
    _cpu: str
    _main_bord: str
    _graphics_card: str

    def __init__(self, builder: 'Builder'):
        self._cpu = builder.cpu
        self._main_bord = builder.main_bord
        self._graphics_card = builder.graphics_card

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, value):
        self._cpu = value

    @property
    def main_bord(self):
        return self._main_bord

    @main_bord.setter
    def main_bord(self, value):
        self._main_bord = value

    @property
    def graphics_card(self):
        return self._graphics_card

    @graphics_card.setter
    def graphics_card(self, value):
        self._graphics_card = value


# 用于创建ComputerBuilder类的Builder
class Builder:
    _cpu: str
    _main_bord: str
    _graphics_card: str

    @property
    def cpu(self):
        return self._cpu

    @property
    def main_bord(self):
        return self._main_bord

    @property
    def graphics_card(self):
        return self._graphics_card

    def builder_cpu(self, value) -> 'Builder':
        self._cpu = value
        return self

    def builder_main_bord(self, value) -> 'Builder':
        self._main_bord = value
        return self

    def builder_graphics_card(self, value) -> 'Builder':
        self._graphics_card = value
        return self

    def builder(self) -> ComputerBuilder:
        return ComputerBuilder(self)
