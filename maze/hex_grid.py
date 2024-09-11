from maze import ColoredGrid
import math
from PIL import Image, ImageDraw

class HexGrid(ColoredGrid):
    # def _prepare_grid(self):
    #     return super()._prepare_grid()

    def _configure_cells(self):
        for elem in self.grid:
            for cell in elem:
                row, col = cell.row, cell.column
                if col % 2 == 0:
                    north_diagonal = row - 1 if row > 0 else None
                    south_diagonal = row
                else:
                    north_diagonal = row
                    south_diagonal = row + 1 if row < self.rows - 1 else None

                if col > 0 and north_diagonal != None: 
                    cell.add_neighbor("northwest", self[north_diagonal, col - 1])
                if col > 0 and south_diagonal != None: 
                    cell.add_neighbor("southwest", self[south_diagonal, col - 1])
                if row > 0: cell.add_neighbor("north", self[row - 1, col])
                if row < self.rows - 1: 
                    cell.add_neighbor("south", self[row + 1, col])
                if row > 0: cell.add_neighbor("north", self[row - 1, col])
                if col < self.columns - 1 and north_diagonal != None: 
                    cell.add_neighbor("northeast", self[north_diagonal, col + 1])
                if col < self.columns - 1 and south_diagonal != None: 
                    cell.add_neighbor("southeast", self[south_diagonal, col + 1])
            
    def to_img(self, cell_size=10, filename="grid.png"):
        a_size = cell_size / 2.0
        b_size = cell_size * math.sqrt(3) / 2.0
        width = cell_size * 2
        height = b_size * 2

        img_width = int((3 * a_size * self.columns + a_size + 0.5))
        img_height = int((height * self.rows + b_size + 0.5))

        img = Image.new(
            "RGBA",
            (img_width + 1, img_height + 1),
            "white"
        )
        draw = ImageDraw.Draw(img)

        for mode in ("background", "cell_border"):
            for cell in self.each_cell():
                cx = cell_size + 3 * cell.column * a_size
                cy = b_size + cell.row * height
                if cell.column % 2 == 1: cy += b_size

                # f, n = far, near
                # n, s, e, w = north, south, east, west
                x_fw = int(cx - cell_size)
                x_nw = int(cx - a_size)
                x_ne = int(cx + a_size)
                x_fe = int(cx + cell_size)

                # m = middle
                y_n = int(cy - b_size)
                y_m = int(cy)
                y_s = int(cy + b_size)

                if mode == "bachgroud":
                    # color background of cell
                    points = [(x_fw, y_m), 
                              (x_nw, y_n),
                              (x_ne, y_n),
                              (x_fe, y_m),
                              (x_ne, y_s),
                              (x_nw, y_s)]
                    draw.polygon(points, 
                                 fill=self.background_color_for(cell),
                                 outline=None,
                                 width=0)
                else:
                    # create black cell for cells not part of the maze
                    # !!!!! to be implemented !!!!!
                    if cell == None:
                        pass
                    else:
                        if cell.neighbor("southwest") == None:
                            draw.line([x_fw, y_m, x_nw, y_s], fill="black")
                        # create boundary northwest unless there is a neighbor up northwest
                        if cell.neighbor("northwest") == None:
                            draw.line([x_fw, y_m, x_nw, y_n], fill="black")
                        # create boundary to the north unless there is a neighbor up north
                        if cell.neighbor("north") == None:
                            draw.line([x_nw, y_n, x_ne, y_n], fill="black")
                        # create boundary to the northeast if no cell is linked
                        if not cell.contains_link(cell.neighbor("northeast")):
                            draw.line([x_ne, y_n, x_fe, y_m], fill="black")
                        # create boundary to the souteast if no cell is linked
                        if not cell.contains_link(cell.neighbor("southeast")):
                            draw.line([x_fe, y_m, x_ne, y_s], fill="black")
                        # create boundary to the south if no cell is linked
                        if not cell.contains_link(cell.neighbor("south")):
                            draw.line([x_ne, y_s, x_nw, y_s], fill="black")

        img.save(filename)


