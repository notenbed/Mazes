from maze import ColoredGrid
from maze import Sidewinder

grid = ColoredGrid(25, 25)
Sidewinder.on(grid)

start = grid[round(grid.rows / 2), round(grid.columns / 2)]
distances = start.distances()
grid.distances(distances.cells)

filename = "colorized_sidewinder.png"
grid.to_img(filename=filename)
print("saved to #", filename)