from maze import Grid
from maze import Wilsons

grid = Grid(20, 20)
Wilsons.on(grid)

filename = "wilsons.png"

grid.to_img(filename=filename)
print("saved to ", filename)