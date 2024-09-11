from maze import DistanceGrid
from maze import BinaryTree

grid = DistanceGrid(5, 5)
BinaryTree.on(grid)
grid.braid(p=0.5)

start = grid[0, 0]
distances = start.distances()

grid.distances = distances.cells

print(grid)

print("path from northwest corener to southwest corner")
grid.distances = distances.path_to(grid[grid.rows - 1, 0])
print(grid)
filename="dijkstra_shortest_path.png"
grid.to_img(filename=filename)