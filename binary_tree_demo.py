from maze import Grid
from maze import BinaryTree

grid = Grid(10, 20)
BinaryTree.on(grid)
print(grid)
grid.to_img(filename="binary_tree_demo.png")

deadends = grid.deadends()
print(str(len(deadends)) + " dead-ends")