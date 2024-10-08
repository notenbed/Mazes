from maze import DistanceGrid
from maze import BinaryTree

grid = DistanceGrid(5, 5)
BinaryTree.on(grid)

start = grid[0, 0]

distances = start.distances()
new_start, distance = distances.max()

new_distances = new_start.distances()
goal, distance = new_distances.max()

grid.distances = new_distances.path_to(goal)

print(grid)