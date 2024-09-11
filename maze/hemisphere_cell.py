from maze import PolarCell

class HemisphereCell(PolarCell):
    def __init__(self, hemisphere, row, column):
        super().__init__(row, column)
        self.hemisphere = hemisphere

    