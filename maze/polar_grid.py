from maze import Grid
from maze import PolarCell

import math
import random
from PIL import Image, ImageDraw

class PolarGrid(Grid):
    def __init__(self, rows):
        super().__init__(rows, 1)


    def _prepare_grid(self):
        rows = [None] * self.rows

        row_height = 1.0 / self.rows
        rows[0] = [PolarCell(0, 0)]

        for row in range(1, self.rows):
            radius = float(row/self.rows)
            circumference = 2 * math.pi * radius

            previous_count = len(rows[row - 1])
            estimated_cell_width = circumference / previous_count
            ratio = round(estimated_cell_width / row_height)

            cells = previous_count * ratio
            rows[row] = [PolarCell(row, col) for col in range(cells)]
        return rows
    
    def _configure_cells(self):
        for cell in self.each_cell():
            row, col = cell.row, cell.column

            if row > 0:
                # the last column has as clockwise neighbor the first column
                if col < len(self.grid[row]) - 1:
                    cell.add_neighbor("cw", self[row, col + 1])
                else:
                    cell.add_neighbor("cw", self[row, 0])
                cell.add_neighbor("ccw", self[row, col])

                ratio = len(self.grid[row]) / len(self.grid[row - 1])
                par_col = int(col / ratio)
                parent = self[row - 1, par_col]
                parent.extend_outward_neighbors(cell)
                cell.add_neighbor("inward", parent)
    
    def __getitem__(self, x):
        return self.grid[x[0]][x[1] % len(self.grid[x[0]])]

    # def random_cell(self):
    #     row = random.randrange(0, self.rows)
    #     col = random.randrange(0, self.columns)
    #     return self[row, col]

    def to_img(self, cell_size=10, filename="grid.png"):
        img_size = 2 * self.rows * cell_size

        background = "white"
        wall = "black"

        img = Image.new(
            "RGBA",
            (img_size + 1, img_size + 1),
            background
        )
        center = img_size / 2
        draw = ImageDraw.Draw(img)

        for cell in self.each_cell():
            if cell.row != 0:
                theta = 2 * math.pi / len(self.grid[cell.row])
                inner_radius = cell.row * cell_size
                outer_radius = (cell.row + 1) * cell_size
                theta_ccw = cell.column * theta
                theta_cw = (cell.column + 1) * theta
                #bottom left of the cell
                ax = center + int(inner_radius * math.cos(theta_ccw))
                ay = center + int(inner_radius * math.sin(theta_ccw))
                #top left of the cell
                bx = center + int(outer_radius * math.cos(theta_ccw))
                by = center + int(outer_radius * math.sin(theta_ccw))
                #bottom right of the cell
                cx = center + int(inner_radius * math.cos(theta_cw))
                cy = center + int(inner_radius * math.sin(theta_cw))
                #top right of the cell
                dx = center + int(outer_radius * math.cos(theta_cw))
                dy = center + int(outer_radius * math.sin(theta_cw))

                if not cell.contains_link(cell.neighbor("cw")):
                    draw.line([cx, cy, dx, dy], fill=wall)

                if not cell.contains_link(cell.neighbor("inward")):
                    draw.line([ax, ay, cx, cy], fill=wall)
        
        ImageDraw.Draw(img).ellipse((0, 
                                     0, 
                                     self.rows * cell_size * 2,
                                     self.rows * cell_size * 2),
                                     outline=wall)
        
        img.save(filename)
