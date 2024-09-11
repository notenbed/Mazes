from maze import Kruskals
from maze import Grid

grid = Grid(20, 20)
Kruskals.on(grid)

filename = "kriskals.png"

grid.to_img(inset=0.1, filename=filename)

print("saved to", filename)