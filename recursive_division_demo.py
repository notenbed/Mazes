from maze import RecursiveDivision
from maze import Grid

grid = Grid(20, 20)

RecursiveDivision.on(grid)



filename="recursive_division.png"
grid.to_img(filename=filename)
print("saved to: ", filename)