from maze import Grid

class CylinderGrid(Grid):

     def __getitem__(self, x):
        if not (x[0] > 0 and x[0] <self.rows): return None
        column = x[1] % (len(self.grid[x[0]]) - 1)
        return self.grid[x[0]][column]