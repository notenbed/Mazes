from maze import Ellers
from maze import ColoredGrid

grid = ColoredGrid(20, 20)

Ellers.on(grid)

start = grid[round(grid.rows / 2), round(grid.columns / 2)]
distances = start.distances()
grid.distances(distances.cells)
filename = "ellers_colored.png"

grid.to_img(filename=filename)
print("saved to: ", filename)