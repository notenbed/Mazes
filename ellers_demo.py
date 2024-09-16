from maze import Ellers
from maze import Grid

grid = Grid(20, 20)

Ellers.on(grid)

filename = "ellers.png"

grid.to_img(filename=filename)
print("saved to: ", filename)