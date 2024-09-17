from maze import Cell

class CubeCell(Cell):
    def __init__(self, face, row, column):
        super().__init__(row, column)
        self.face = face
