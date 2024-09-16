from maze import GrowingTree
from maze import ColoredGrid
import random

def select_random(lst):
    return random.choice(lst)

def select_last(lst):
    return lst[-1]

def mix(lst):
    if random.randint(0, 1) == 0:
        elem = random.choice(lst)
    else:
        elem = lst[-1]
    return elem

def save(grid, filename):
    grid.to_img(filename=filename)
    print("saved to: ", filename)

grid = ColoredGrid(20, 20)
start = grid.random_cell()
row, column = start.row, start.column
GrowingTree.on(select_random, grid, start_at=start)
distances = start.distances()
grid.distances(distances.cells)
save(grid, "growing_tree_random.png")

grid = ColoredGrid(20, 20)
start = grid[row, column]
GrowingTree.on(select_random, grid, start_at=start)
distances = start.distances()
grid.distances(distances.cells)
save(grid, "growing_tree_last.png")

grid = ColoredGrid(20, 20)
start = grid[row, column]
GrowingTree.on(select_random, grid, start_at=start)
distances = start.distances()
grid.distances(distances.cells)
save(grid, "growing_tree_mix.png")
