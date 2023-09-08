
class Computer:
    _cpu: str
    _main_bord: str
    _graphics_card: str

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
