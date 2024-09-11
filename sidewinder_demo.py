from maze import Grid
from maze import Sidewinder

grid = Grid(10, 15)
Sidewinder.on(grid)

print(grid)
grid.to_img(filename="sidewinder_demo.png")