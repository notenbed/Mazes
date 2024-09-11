from maze import ColoredGrid
from maze import RecursiveBacktracker

grid = ColoredGrid(25, 25)
RecursiveBacktracker.on(grid)

start = grid[round(grid.rows / 2), round(grid.columns / 2)]
distances = start.distances()
grid.distances(distances.cells)

filename = "colorized_recursive_backtracker.png"
grid.to_img(filename=filename)
print("sved to ", filename)