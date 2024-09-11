from maze import Cell
from maze import Distances

class WeightedCell(Cell):
    def __init__(self, row, column):
        super().__init__(row, column)
        self.weight = 1

    def distances(self):
        weights = Distances(self)
        pending = [self]

        while len(pending) > 0:
            pending.sort(key=lambda x: weights[x])
            cell = pending[0]
            pending.remove(cell)
            for neighbor in cell.get_links():
                total_weight = weights[cell] + neighbor.weight
                
                if weights[neighbor] == None or total_weight < weights[neighbor]:
                    pending.append(neighbor)
                    weights[neighbor] = total_weight

        return weights