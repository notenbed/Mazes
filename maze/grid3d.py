from maze import Grid
from maze import Cell3D
from PIL import Image, ImageDraw
import random

class Grid3D(Grid):
    def __init__(self, levels, rows, columns):
        self.levels = levels
        super().__init__(rows, columns)

    def _prepare_grid(self):
        return [[[Cell3D(level, row, col) for level in range(self.levels)]
                 for col in range(self.columns)]
                 for row in range(self.rows)]
    
    def _configure_cells(self):
        for level in self.grid:
            for row in level:
                for cell in row:
                    level, row, col = cell.level, cell.row, cell.column
                    
                    cell.add_neighbor("north", self[level, row - 1, col])
                    cell.add_neighbor("south", self[level, row + 1, col])
                    cell.add_neighbor("west", self[level, row, col - 1])
                    cell.add_neighbor("east", self[level, row, col + 1])
                    cell.add_neighbor("down", self[level - 1, row, col])
                    cell.add_neighbor("up", self[level + 1, row, col])

    def __getitem__(self, x):
        row = x[0]
        col = x[1]
        level = x[2]
        if row in range(0, self.rows) and col in range(0, self.columns) and level in range(0, self.levels):
            return self.grid[row][col][level]
        else:
            return None
    
    def random_cell(self):
        level = random.randint(0, self.levels - 1)
        row = random.randint(0, self.rows - 1)
        column = random.randint(0, self.columns - 1)
        return self[level, row, column]

    def size(self):
        return self.levels * self.rows, self.columns
    
    def each_level(self):
        for level in self.grid:
            yield level
    
    def each_row(self):
        for level in self.each_level():
            for row in level:
                yield row

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell
    
    def to_img(self, cell_size=10, inset=0.0, margin=None, filename="grid.png"):
        if margin == None: margin = int(cell_size/2)
        inset = int(cell_size * inset)

        grid_witdth = cell_size * self.columns
        grid_height = cell_size * self.rows

        img_width = grid_witdth * self.levels + (self.levels - 1) * margin
        img_height = grid_height

        wall = "black"
        background = "white"
        arrow = "blue"

        img = Image.new(
            "RGBA",
            (img_width + 1, img_height + 1),
            background
        )
        draw = ImageDraw.Draw(img)

        for mode in ("background", "walls"):
            for cell in self.each_cell():
                x = cell.level * (grid_witdth + margin) + cell.column * cell_size
                y = cell.row * cell_size

                if inset > 0:
                    super().__to_png_with_inset(draw, cell, mode, cell_size,  wall, x, y, inset)
                else:
                    super()._to_png_without_inset(draw, cell, mode, cell_size, wall, x, y)

                if mode == "walls":
                    mid_x = x + cell_size / 2
                    mid_y = y + cell_size / 2

                    if cell.contains_link(cell.neighbor("down")):
                        draw.line([mid_x - 3, mid_y, mid_x - 1, mid_y + 2],
                                  fill=arrow)
                        draw.line([mid_x - 3, mid_y, mid_x - 1, mid_y - 2],
                                  arrow)
                        
                    if cell.contains_link(cell.neighbor("up")):
                        draw.line([mid_x + 3, mid_y, mid_x + 1, mid_y + 2],
                                  arrow)
                        draw.line([mid_x + 3, mid_y, mid_x + 1, mid_y - 2],
                                  arrow)
        img.save(filename)                        
    
