from maze import Grid
from maze import RecursiveBacktracker

grid = Grid(5, 5)

# orphan the cell in the northwest corner...
grid[0, 0].neighbor("east").remove_neighbor("west")
grid[0, 0].neighbor("south").remove_neighbor("north")

# ... and the one in the southest corner
grid[4, 4].neighbor("west").remove_neighbor("east")
grid[4, 4].neighbor("north").remove_neighbor("south")

RecursiveBacktracker.on(grid, start_at=grid[1, 1])

print(grid)