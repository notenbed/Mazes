from maze import Grid
from maze import Cell

class MaskedGrid(Grid):
    def __init__(self, mask):
        self.mask = mask
        super().__init__(self.mask.rows, self.mask.columns)

    def _prepare_grid(self):
        maze = []
        for row in range(self.rows):
            r = []
            for col in range(self.columns):
                if self.mask[row, col]:
                    r.append(Cell(row, col))
                else:
                    r.append(None)
            maze.append(r)
        return maze
    
    def _configure_cells(self):
        for elem in self.grid:
            for cell in elem:
                if cell != None:
                    row, col = cell.row, cell.column
                    if col > 0 and self.mask[row, col -1]: cell.add_neighbor("west", self.grid[row][col - 1])
                    if col < self.columns - 1 and self.mask[row, col + 1]: cell.add_neighbor("east", self.grid[row][col + 1])
                    if row > 0 and self.mask[row - 1, col]: cell.add_neighbor("north", self.grid[row - 1][col])
                    if row < self.rows - 1 and self.mask[row + 1, col]: cell.add_neighbor("south", self.grid[row + 1][col])

    def random_cell(self):
        row, col = self.mask.random_location()
        return self[row, col]
    
    def size(self):
        return len(self.mask)