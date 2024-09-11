from maze import Grid
import math
from PIL import Image, ImageDraw

class TriangleGrid(Grid):
    def _configure_cells(self):
        for cell in self.each_cell():
            row, col = cell.row, cell.column

            if col > 0:
                cell.add_neighbor("west", self[row, col - 1])
            if col < self.columns - 1:
                cell.add_neighbor("east", self[row, col + 1])
            
            if (row + col) % 2 == 0:
                if row < self.rows - 1:
                    cell.add_neighbor("south", self[row + 1, col])
            elif row > 0:
                cell.add_neighbor("north", self[row - 1, col])

    def to_img(self, cell_size=16, filename="grid.png"):
        half_width = cell_size / 2.0
        height = cell_size * math.sqrt(3) / 2.0
        half_height = height / 2.0

        img_width = int((cell_size * (self.columns + 1) / 2.0))
        img_height = int(height * self.rows)

        img = Image.new(
            "RGBA",
            (img_width + 1, img_height + 1),
            "white"
        )

        draw = ImageDraw.Draw(img)

        for mode in ("background", "cell_border"):
            for cell in self.each_cell():
                row, col = cell.row, cell.column
                cx = half_width + col * half_width
                cy = half_height + row * height

                west_x = int(cx - half_width)
                mid_x = int(cx)
                east_x = int(cx + half_width)
                upright = (col + row) % 2 == 0
                if upright:
                    apex_y = int(cy - half_height)
                    base_y = int(cy + half_height)
                else:
                    apex_y = int(cy + half_height)
                    base_y = int(cy - half_height)

                if mode == "background":
                    # color bachgroud of cell
                    color = self.background_color_for(cell)
                    if color:
                        points =[(west_x, base_y),
                                 (mid_x, apex_y),
                                 (east_x, base_y)]
                        draw.polygon(points,
                                     fill=color,
                                     outline=None,
                                     width=0)
                else:
                    if cell.neighbor("west") == None:
                        draw.line([west_x, base_y, mid_x, apex_y], fill="black")
                    if not cell.contains_link(cell.neighbor("east")):
                        draw.line([east_x, base_y, mid_x, apex_y], fill="black")

                    no_south = upright and not cell.neighbor("south")
                    not_linked = not upright and not cell.contains_link(cell.neighbor("north"))

                    if no_south or not_linked:
                        draw.line([east_x, base_y, west_x, base_y], fill="black")

        img.save(filename)
