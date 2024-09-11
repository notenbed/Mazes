from maze import Grid
from maze import BinaryTree
from maze import Sidewinder
from maze import AldousBroder
from maze import HuntAndKill

algorithms = [BinaryTree, Sidewinder, AldousBroder, HuntAndKill]

tries = 100
size = 20

averages = {}
for algo in algorithms:
    print("running ", algo.__name__)

    deadend_counts = []
    for _ in range(tries):
        grid = Grid(size, size)
        algo.on(grid)
        deadend_counts.append(len(grid.deadends()))
    
    total_deadends = sum(deadend_counts)
    averages[algo] = total_deadends / len(deadend_counts)

total_cells = size * size
print()
print("Average dead-ends per {} x {} maze {} cells:".format(size, size, total_cells))
print()

sorted_algorithms = dict(sorted(averages.items(), key=lambda item: item[1])).keys()

for algo in sorted_algorithms:
    percentage = averages[algo] * 100 / (size * size)
    print("%14s : %3d/%d (%d%%)" % (algo.__name__, averages[algo], total_cells, percentage))
