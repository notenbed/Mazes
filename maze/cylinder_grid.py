from maze import Grid

class CylinderGrid(Grid):

     def __getitem__(self, x):
        row, column = x
        if row not in range(0, self.rows): return None
        column = column % (len(self.grid[row]) - 1)
        return self.grid[row][column]