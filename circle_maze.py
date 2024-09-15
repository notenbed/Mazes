from maze import PolarGrid
from maze import RecursiveBacktrackerCircle

grid = PolarGrid(8)
RecursiveBacktrackerCircle.on(grid)

filename = "cicle_maze.png"
grid.to_img(filename=filename)

print("saved to ", filename)