from builder import Builder
from computer import Computer


class Directory:
    _builder: Builder

    def __init__(self, builder: Builder):
        self._builder = builder

    def construct(self) -> Computer:
        self._builder.create_main_bord()
        self._builder.create_cpu()
        self._builder.create_graphics_card()
        return self._builder.create_computer()
