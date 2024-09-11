from maze import Cell

class Cell3D(Cell):
    def __init__(self, level, row, column):
        super().__init__(row, column)
        self.level = level

    def neighbors(self):
        lst = super().neighbors()
        if self.neighbor("up") != None: lst.append(self.neighbor("up"))
        if self.neighbor("down") != None: lst.append(self.neighbor("down"))
        return lst
    