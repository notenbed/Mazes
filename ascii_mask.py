from maze import Mask
from maze import MaskedGrid
from maze import RecursiveBacktracker

import sys

mask_file = sys.argv[1]
print("mask file: ", mask_file)
mask = Mask.from_txt(mask_file)
grid = MaskedGrid(mask)
RecursiveBacktracker.on(grid)

filename = "masked.png"
grid.to_img(filename=filename)

print("saved image to ", filename)