from maze import Cell

class CubeCell(Cell):
    def __init__(self, face, row, column):
        super().__init__(row, column)
        self.face = face

    def neighbors(self):
        neighbor_list = []
        if self.neighbor("north") != None: neighbor_list.append(self.neighbor("north"))
        if self.neighbor("south") != None: neighbor_list.append(self.neighbor("south"))
        if self.neighbor("east") != None: neighbor_list.append(self.neighbor("east"))
        if self.neighbor("west") != None: neighbor_list.append(self.neighbor("west"))
        return neighbor_list

    def remove_neighbor(self, key):
        self._neighbors[key] = None
 