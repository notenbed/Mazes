from maze import SphereGrid
from maze import RecursiveBacktracker

grid = SphereGrid(20)
RecursiveBacktracker.on(grid)

filename = "sphere_map.png"
grid.to_img(filename=filename)
print("saved to: ", filename)