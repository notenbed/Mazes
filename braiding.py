from maze import RecursiveBacktracker
from maze import Grid

grid = Grid(20, 20)
RecursiveBacktracker.on(grid)

filename="grid_without_braiding.png"
grid.to_img(filename=filename)

print("saved to ", filename)

filename = "grid_with_braiding.png"
grid.braid(p=0.5)
grid.to_img(filename=filename)

print("saved to ", filename)