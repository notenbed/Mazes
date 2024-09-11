from maze import ColoredGrid
from maze import BinaryTree

grid = ColoredGrid(25, 25)
BinaryTree.on(grid)

start = grid[round(grid.rows / 2), round(grid.columns / 2)]
distances = start.distances()
grid.distances(distances.cells)

filename = "colorized_binarytree.png"
grid.to_img(filename=filename)
print("saved to ", filename)