from maze import RecursiveBacktracker
from maze import Grid

grid = Grid(20, 20)
RecursiveBacktracker.on(grid)

filename="recursive_bakctracker.png"
grid.to_img(filename=filename)
print("saved to ", filename)