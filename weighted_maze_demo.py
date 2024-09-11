from maze import WeightedGrid
from maze import RecursiveBacktracker
#import random

grid = WeightedGrid(10, 10)
RecursiveBacktracker.on(grid)

grid.braid(p=0.5)
start, finish = grid[0, 0], grid[grid.rows - 1, grid.columns - 1]

distances = start.distances()
farthest, grid.maximum = distances.max()
grid.distances = distances.path_to(finish)
print(grid)

filename = "path_without_weight_obstacle.png"
grid.to_img(filename=filename)
print("saved to ", filename)

lava = grid.random_cell()
lava.weight = 50

grid.distances = start.distances().path_to(finish)

filename = "paht_with_weight_obstacle.png"
grid.to_img(filename=filename)
print("saved to ", filename)