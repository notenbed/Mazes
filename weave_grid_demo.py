from maze import RecursiveBacktracker
from maze import WeaveGrid

grid = WeaveGrid(20, 20)
RecursiveBacktracker.on(grid)

filename="weave.png"
grid.to_img(filename=filename)

print("saved to ", filename)