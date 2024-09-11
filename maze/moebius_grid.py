from maze import CylinderGrid
from PIL import Image, ImageDraw

class MoebiusGrid(CylinderGrid):
    def __init__(self, rows, columns):
        super().__init__(rows, columns * 2)
    
    def to_img(self, cell_size=20, inset=0, filename="grid.png"):
        grid_height = cell_size * self.rows
        mid_point = int(self.columns / 2)

        img_width = cell_size * mid_point
        img_height = grid_height * 2

        inset = int((cell_size * inset))

        background = "white"
        wall = "black"

        img = Image.new(
            "RGBA",
            (img_width + 1, img_height + 2),
            background
        )
        draw = ImageDraw.Draw(img)


        for mode in ["background", "walls"]:
            for cell in self.each_cell():
                x = (cell.column % mid_point) * cell_size
                y = cell.row * cell_size

                if cell.column >= mid_point: y += grid_height

                if inset > 0:
                    self._to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
                else:
                    self._to_png_without_inset(draw, cell, mode, cell_size, wall, x, y)

        img.save(filename)
