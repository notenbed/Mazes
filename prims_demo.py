from maze import SimplifiedPrims
from maze import TruePrims
from maze import ColoredGrid

grid = ColoredGrid(20, 20)

start = grid.random_cell()
row, column = start.row, start.column
SimplifiedPrims.on(grid, start_at=start)

distances = start.distances()
grid.distances(distances.cells)

filename = "prims_simple.png"
grid.to_img(filename=filename)
print("saved to: ", filename)

grid = ColoredGrid(20, 20)
start = grid[row, column]
TruePrims.on(grid, start_at=start)

distances = start.distances()
grid.distances(distances.cells)

filename = "prims_true.png"
grid.to_img(filename=filename)
print("saved to ", filename)
