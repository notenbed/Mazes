from maze import RecursiveBacktracker
from maze import WeaveGridColored

grid = WeaveGridColored(20, 20)
RecursiveBacktracker.on(grid)

start = grid[round(grid.rows / 2), round(grid.columns / 2)]
distances = start.distances()
grid.distances(distances.cells)

filename="weave_colored.png"
grid.to_img(filename=filename)

print("saved to ", filename)