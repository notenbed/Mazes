from maze import RecursiveBacktracker
from maze import ColoredGrid

grid = ColoredGrid(20, 20)
RecursiveBacktracker.on(grid)

start = grid[round(grid.rows / 2), round(grid.columns / 2)]
distances = start.distances()
grid.distances(distances.cells)

filename="recursive_bakctracker_with_inset_colored.png"
grid.to_img(inset=0.1, filename=filename)
print("saved to ", filename)

filename="recursive_backtracker_without_inset_colored.png"
grid.to_img(filename=filename)
print("saved to ", filename)