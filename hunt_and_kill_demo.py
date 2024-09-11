from maze import Grid
from maze import HuntAndKill

grid = Grid(20, 20)
HuntAndKill.on(grid)

filename = "hunt_and_kill.png"
grid.to_img(filename=filename)
print("saved to ", filename)