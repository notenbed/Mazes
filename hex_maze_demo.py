from maze import RecursiveBacktracker
from maze import HexGrid

grid = HexGrid(10, 10)
RecursiveBacktracker.on(grid)

filename = "hex_grid.png"
grid.to_img(filename=filename)

print("saved to ", filename)