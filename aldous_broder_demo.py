from maze import Grid
from maze import AldousBroder

grid = Grid(20, 20)
AldousBroder.on(grid)

file_name = "aldous_broder.png"
grid.to_img(filename=file_name)

print("saved to #", file_name)