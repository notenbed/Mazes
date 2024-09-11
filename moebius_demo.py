from maze import MoebiusGrid
from maze import RecursiveBacktracker

grid = MoebiusGrid(5, 50)
RecursiveBacktracker.on(grid)

filename = "moebius.png"
grid.to_img(filename=filename)
print("saved to: ", filename)