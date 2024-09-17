from maze import ColoredGrid
from maze import OverCell
from maze import UnderCell

class WeaveGridColored(ColoredGrid):
    def __init__(self, rows, columns):
        self.under_cells = []
        super().__init__(rows, columns)
    
    def _prepare_grid(self):
        maze = [[OverCell(row, col, self) for col in range(self.columns)] 
        for row in range(self.rows)]
        
        return maze

    def _configure_cells(self):
        for elem in self.grid:
            for cell in elem:
                row, col = cell.row, cell.column
                cell.add_neighbor("west", self[row, col - 1])
                cell.add_neighbor("east", self[row, col + 1])
                cell.add_neighbor("north", self[row - 1, col])
                cell.add_neighbor("south", self[row + 1, col])
    
    def tunnel_under(self, over_cell):
        under_cell = UnderCell(over_cell)
        self.under_cells.append(under_cell)
    
    def each_cell(self):
        for row in self.grid:
            for cell in row:
                yield cell

        for under_cell in self.under_cells:
            yield under_cell
    
    def to_img(self, cell_size=20, inset=None, filename="grid.png"):
        super().to_img(cell_size, inset=(inset or 0.1), filename=filename)

    def _to_png_with_inset(self, draw, cell, mode, cell_size, wall, x, y, inset):
        if isinstance(cell, OverCell):
            super()._to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
        else:
            x1, x2, x3, x4, y1, y2, y3, y4 = self._cell_coordinates_with_inset(x, y, cell_size, inset)

            if cell.vertical_passage():
                draw.line([x2, y1, x2, y2],
                          fill=wall)
                draw.line([x3, y1, x3, y2],
                          fill=wall)
                draw.line([x2, y3, x2, y4],
                          fill=wall)
                draw.line([x3, y3, x3, y4],
                          fill=wall)
            else:
                draw.line([x1, y2, x2, y2],
                          fill=wall)
                draw.line([x1, y3, x2, y3],
                          fill=wall)
                draw.line([x3, y2, x4, y2],
                          fill=wall)
                draw.line([x3, y3, x4, y3],
                          fill=wall)