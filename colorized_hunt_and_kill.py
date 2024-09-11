from maze import ColoredGrid
from maze import HuntAndKill

grid = ColoredGrid(25, 25)
HuntAndKill.on(grid)

start = grid[round(grid.rows / 2), round(grid.columns / 2)]
distances = start.distances()
grid.distances(distances.cells)

filename = "colorized_hunt_and_kill.png"
grid.to_img(filename=filename)
print("saved to ", filename)