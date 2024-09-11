from maze import Cell

class PolarCell(Cell):
    def __init__(self, row, column):
        super().__init__(row, column)
        self._outward = []
        self.add_neighbor("outward", self._outward)
        
    def extend_outward_neighbors(self, cell):
        self._neighbors["outward"].append(cell)

    def each_neighbor(self):
        for key, neighbor in self._neighbors.items():
            if key == "outward" :
                for elem in self._neighbors['outward']:
                    yield elem
            else:
                yield neighbor
