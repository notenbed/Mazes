from maze import Grid
from maze import CubeCell
from PIL import Image, ImageDraw
import random

class CubeGrid(Grid):
    def __init__(self, dim):
        super().__init__(dim, dim)
        

    def _prepare_grid(self):
        # return [[[CubeCell(face, row, column) for face in range(0, 6)]
        #          for column in range(self.columns)]
        #          for row in range(self.rows)]
        lst = []
        for face in range(6):
            lst.append([])
            for row in range(self.rows):
                lst[face].append([])
                for col in range(self.columns):
                    lst[face][row].append(CubeCell(face, row, col))

        return lst
            
    def _configure_cells(self):
        for cell in self.each_cell():
            face, row, column = cell.face, cell.row, cell.column

            cell.add_neighbor("west", self[face, row, column - 1])
            cell.add_neighbor("east", self[face, row, column + 1])
            cell.add_neighbor("north", self[face, row - 1, column])
            cell.add_neighbor("south", self[face, row + 1, column])

    def wrap(self, face, row, column):

        n = self.rows - 1

        # to get it working for rectangular objects the following is necessary
        # dim_r = self.rows - 1
        # dim_c = self.columns - 1

        if row < 0:
            if face == 0: return [4, column, 0]
            if face == 1: return [4, n, column]
            if face == 2: return [4, n - column, n]
            if face == 3: return [4, 0, n - column]
            if face == 4: return [3, 0, n - column]
            if face == 5: return [1, n, column]
        elif row >= self.rows:
            if face == 0: return [5, n - column, 0]
            if face == 1: return [5, 0, column]
            if face == 2: return [5, column, n]
            if face == 3: return [5, n, n - column]
            if face == 4: return [1, 0, column]
            if face == 5: return [3, n, n - column]
        elif column < 0:
            if face == 0: return [3, row, n]
            if face == 1: return [0, row, n]
            if face == 2: return [1, row, n]
            if face == 3: return [2, row, n]
            if face == 4: return [0, 0, row]
            if face == 5: return [0, n, n - row]
        elif column >= self.columns:
            if face == 0: return [1, row, 0]
            if face == 1: return [2, row, 0]
            if face == 2: return [3, row, 0]
            if face == 3: return [0, row, 0]
            if face == 4: return [2, 0, n - row]
            if face == 5: return [2, n, row]

        return face, row, column
    
    def __getitem__(self, x):
        if x[0] < 0 or x[0] >= 6: return None
        face, row, column = self.wrap(x[0], x[1], x[2])
        return self.grid[face][row][column]
    
    def each_face(self):
        for face in self.grid:
            yield face
    
    def each_row(self):
        for face in self.each_face():
            for row in face:
                yield row

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell

    def random_cell(self):
        face = random.randint(0, 5)
        row = random.randint(0, self.rows)
        column = random.randint(0, self.columns)

        return self[face, row, column]
    
    def size(self):
        return 6 * self.rows * self.columns
    
    def draw_outlines(self, img, height, width, outline):
        # face #0
        img.rectangle((0, height, width, height * 2),
                      fill=None,
                      outline=outline,
                      width=1)
        
        # face #2 & face #3
        img.rectangle((width * 2, height, width * 4, height * 2),
                      fill=None,
                      outline=outline,
                      width=1)
        
        # face #4
        img.rectangle((width, 0, width * 2, height),
                      fill=None,
                      outline=outline,
                      width=1)
        
        # face #5
        img.rectangle((width, height * 2, width * 2, height * 3),
                      fill=None,
                      outline=outline,
                      width=1)
    
    def to_img(self, cell_size=20, inset=0, filename="grid.png"):
        inset = int(cell_size * inset)

        face_width = cell_size * self.columns
        face_height = cell_size * self.rows

        img_width = 4 * face_width
        img_height = 3 * face_height

        offsets = [[0, 1], [1, 1], [2, 1], [3, 1], [1, 0], [ 1, 2]]

        background = "white"
        wall = "black"
        outline = (100, 0, 0)

        img = Image.new(
            "RGBA",
            (img_width + 1, img_height + 1),
            background
        )
        draw = ImageDraw.Draw(img)

        self.draw_outlines(draw, face_width, face_height, outline)

        for mode in ["background", "wall"]:
            for cell in self.each_cell():
                x = offsets[cell.face][0] * face_width + cell.column * cell_size
                y = offsets[cell.face][1] * face_height + cell.row * cell_size

                if inset > 0:
                    self._to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
                else:
                    self._to_png_without_inset(draw, cell, mode, cell_size, wall, x, y)

        img.save(filename)

    def _to_png_without_inset(self, img, cell, mode, cell_size, wall, x, y):
        x1, y1 = x, y
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        if mode == "background":
            color = self.background_color_for(cell)
            if color != None:
                img.rectangle(((x, y, x2, y2)),
                              fill=color,
                              outline=None,
                              width=0)
        else:
            if cell.neighbor("north").face != cell.face and not cell.contains_link(cell.neighbor("north")):
                img.line([x1, y1, x2, y1],
                            fill=wall)
                
            if cell.neighbor("west").face != cell.face and not cell.contains_link(cell.neighbor("west")):
                img.line([x1, y1, x1, y2],
                            fill=wall)
            
            if cell.contains_link(cell.neighbor("east")): img.line([x2, y1, x2, y2], fill=wall)
            if cell.contains_link(cell.neighbor("south")): img.line([x1, y2, x2, y2], fill=wall)