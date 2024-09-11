from maze import HexGrid
from maze import RecursiveBacktracker

# !!!!!! IS NOT WORKING !!!!!!!!!!!


grid = HexGrid(25, 25)
RecursiveBacktracker.on(grid)

start = grid[round(grid.rows / 2), round(grid.columns / 2)]
distances = start.distances()
grid.distances(distances.cells)

filename = "colorized_hex_grid.png"
grid.to_img(filename=filename)
print("saved to ", filename)