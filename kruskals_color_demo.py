from maze import Kruskals
from maze import ColoredGrid

grid = ColoredGrid(20, 20)
Kruskals.on(grid)

filename = "kriskals_colored.png"

start = grid[round(grid.rows / 2), round(grid.columns / 2)]
distances = start.distances()
grid.distances(distances.cells)

grid.to_img(filename=filename)

print("saved to", filename)