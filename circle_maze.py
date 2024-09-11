from maze import PolarGrid
from maze import RecursiveBacktracker

grid = PolarGrid(8)
RecursiveBacktracker.on(grid)

filename = "cicle_maze.png"
grid.to_img(filename=filename)

print("saved to ", filename)