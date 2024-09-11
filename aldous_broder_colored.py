from maze import ColoredGrid
from maze import AldousBroder

for n in range(6):
    grid = ColoredGrid(20, 20)
    AldousBroder.on(grid)

    start = grid[round(grid.rows / 2), round(grid.columns / 2)]
    distances = start.distances()
    grid.distances(distances.cells)

    filename = "aldous_broder_%02d.png" % n
    grid.to_img(filename=filename)
    print("saved to ", filename)