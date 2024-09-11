from maze import Kruskals
from maze import WeaveGrid
from maze import OverCell
import random

class SimpleOverCell(OverCell):
    def neighbors(self):
        neighbor_list = []
        if self.neighbor("north"): neighbor_list.append(self.neighbor("north"))
        if self.neighbor("south"): neighbor_list.append(self.neighbor("south"))
        if self.neighbor("east"): neighbor_list.append(self.neighbor("east"))
        if self.neighbor("west"): neighbor_list.append(self.neighbor("west"))
        return neighbor_list
    
class PreconfigureGrid(WeaveGrid):
    def _prepare_grid(self):
        maze = [[SimpleOverCell(row, col, self) for col in range(self.columns)]
                 for row in range(self.rows)]
        return maze


grid = PreconfigureGrid(20, 20)
state = Kruskals.State(grid)


for i in range(grid.size()):
    row = random.randint(1, grid.rows - 1)
    col = random.randint(1, grid.columns - 1)
    state.add_crossing(grid[row, col])


Kruskals.on(grid, state=state)

filename = "kriskals_weave.png"

grid.to_img(inset=0.2,filename=filename)

print("saved to", filename)