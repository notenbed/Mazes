from maze import RecursiveBacktracker
from maze import TriangleGrid

grid = TriangleGrid(10, 17)
RecursiveBacktracker.on(grid)
filename = "delta.png"
grid.to_img(filename=filename)

print("saved to ", filename)