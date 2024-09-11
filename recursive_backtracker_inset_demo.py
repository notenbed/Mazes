from maze import RecursiveBacktracker
from maze import Grid

grid = Grid(20, 20)
RecursiveBacktracker.on(grid)

filename="recursive_bakctracker_with_inset.png"
grid.to_img(inset=0.1, filename=filename)
print("saved to ", filename)

filename="recursive_backtracker_without_inset.png"
grid.to_img(filename=filename)
print("saved to ", filename)