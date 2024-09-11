from maze import CylinderGrid
from maze import RecursiveBacktracker

grid = CylinderGrid(7, 16)
RecursiveBacktracker.on(grid)

filename = "cylinder.png"
grid.to_img(filename=filename)
print("saved to: ", filename)