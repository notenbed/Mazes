from maze import Grid
from maze import WeightedCell

from PIL import Image, ImageDraw

class WeightedGrid(Grid):

    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = {}
        self.maximum = 1

    def _prepare_grid(self):
        maze = [[WeightedCell(row, col) for col in range(self.columns)] 
        for row in range(self.rows)]

        return maze
    
    def background_color_for(self, cell):
        color = None
        if cell.weight > 1:
            color = (255, 0, 0)
        elif len(self.distances) > 0:
            if cell in self.distances:
                distance = self.distances[cell]
                intensity = int(64 + 191 * (self.maximum - distance) / self.maximum)
                color = (intensity, intensity, 0)
        return color
