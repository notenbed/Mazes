from maze import Grid3D
from maze import RecursiveBacktracker

grid = Grid3D(3, 3, 3)
RecursiveBacktracker.on(grid)

filename="3d.png"
grid.to_img(cell_size=20, filename=filename)
print("saved to: ", filename)