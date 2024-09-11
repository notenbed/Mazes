from maze import Mask
from maze import MaskedGrid
from maze import RecursiveBacktracker

mask = Mask(5, 5)

mask[0, 0] = False
mask[2, 2] = False
mask[4, 4] = False

grid = MaskedGrid(mask)
RecursiveBacktracker.on(grid)

print(grid)

filename = "simple_mask_demo.png"
grid.to_img(filename=filename)
print("ssaved to ", filename)