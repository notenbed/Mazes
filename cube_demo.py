from maze import CubeGrid
from maze import RecursiveBacktracker

grid = CubeGrid(10)
RecursiveBacktracker.on(grid)

filename = "cube.png"
grid.to_img(filename=filename)
print("saved to: ", filename)