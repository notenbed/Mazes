from maze import Cell
import random
from PIL import Image, ImageDraw

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self._prepare_grid()
        self._configure_cells()

    
    def _prepare_grid(self):
        return [[Cell(row, col) for col in range(self.columns)] 
        for row in range(self.rows)]
    
    def _configure_cells(self):
        for elem in self.grid:
            for cell in elem:
                row, col = cell.row, cell.column
                cell.add_neighbor("west", self[row, col - 1])
                cell.add_neighbor("east", self[row, col + 1])
                cell.add_neighbor("north", self[row - 1, col])
                cell.add_neighbor("south", self[row + 1, col])

    def __getitem__(self, x):
        row, col = x
        if row in range(0, self.rows) and col in range(0, self.columns):
            return self.grid[row][col]
        else:
            return None
    
    def size(self):
        return self.rows * self.columns
    
    def random_cell(self):
        ch = random.choice(self.grid)
        return random.choice(ch)
    
    def each_row(self):
        for row in self.grid:
            yield row

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell

    def deadends(self):
        return [cell for cell in self.each_cell() 
                if len(cell.get_links()) == 1]
    
    def contents_of(self, cell):
        return " "
    
    def background_color_for(self, cell):
        return None
    
    def braid(self, p=1.0):
        dead = self.deadends()
        random.shuffle(dead)
        for cell in dead:
            if len(cell.links) != 1 or random.random() > p:
                continue
            neighbors = [x for x in cell.neighbors() if not cell.contains_link(x)]
            best = [x for x in neighbors if len(x.get_links()) == 1]
            if len(best) == 0: best = neighbors
            neighbor = random.choice(best)
            cell.link(neighbor)

    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"

        for row in self.each_row():
            top = "|"
            bottom = "+"

            for cell in row:
                if cell == None:
                    body = "   "
                    east_boundary = "|"
                    south_boundary = "---"
                else:
                    body = " " + self.contents_of(cell) + " "
                    east_boundary = " " if cell.contains_link(cell.neighbor("east")) else "|"

                    south_boundary = "   " if cell.contains_link(cell.neighbor("south")) else "---"
                top += body + east_boundary
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"

        return output
    


    def to_img(self, cell_size=20, inset=0.0, filename="grid.png"):

        cell_border = 2
        wall = "black"
        # Create a white canvas
        img = Image.new(
            "RGBA",
            (self.columns * cell_size, self.rows * cell_size),
            "white"
        )
        draw = ImageDraw.Draw(img)

        # create frame around the maze
        draw.rectangle((0, 0, self.columns * cell_size, self.rows * cell_size),
                       fill=None, 
                       outline="white", 
                       width = cell_border)
        inset = int((cell_size * inset))
        

        for mode in ("background", "cell_border"):

            for cell in self.each_cell():
                x = cell.column * cell_size
                y = cell.row * cell_size

                if inset > 0:
                    self._to_png_with_inset(draw, cell, mode, cell_size, wall, x, y, inset)
                else:
                    self._to_png_without_inset(draw, cell, mode, cell_size, wall, x, y)

        img.save(filename)

    def _cell_coordinates_with_inset(self, x, y, cell_size, inset):
        x1, x4 = x, x + cell_size
        x2 = x1 + inset
        x3 = x4 - inset

        y1, y4 = y, y + cell_size
        y2 = y1 + inset
        y3 = y4 - inset
        return [x1, x2, x3, x4, y1, y2, y3, y4]
    
    def _to_png_with_inset(self, draw, cell, mode, cell_size,  wall, x, y, inset):
        x1, x2, x3, x4, y1, y2, y3, y4 = self._cell_coordinates_with_inset(x, y, cell_size, inset)

        if mode == "backgrounds":
            draw.rectangle((x2, y2, x3, y3),
                            fill=self.background_color_for(cell),
                            outline=None,
                            width=0)
            if cell.contains_link(cell.neighbor("north")):
                draw.rectangle((x2, y1, x3, y2),
                                fill=self.background_color_for(cell),
                                outline=None,
                                width=0)
            if cell.contains_link(cell.neighbor("south")):
                draw.rectangle((x2, y3, x3, y4),
                                fill=self.background_color_for(cell),
                                outline=None,
                                width=0)
            if cell.contains_link(cell.neighbor("west")):
                draw.rectangle((x1, y2, x2, y3),
                                fill=self.background_color_for(cell),
                                outline=None,
                                width=0)
            if cell.contains_link(cell.neighbor("east")):
                draw.rectangle((x3, y2, x4, y3),
                                fill=self.background_color_for(cell),
                                outline=None,
                                width=0)
        else:
            if cell.contains_link(cell.neighbor("north")):
                draw.line([x2, y1, x2, y2],
                            fill=wall)
                draw.line([x3, y1, x3, y2],
                            fill=wall)
            else:
                draw.line([x2, y2, x3, y2],
                            fill=wall)
            if cell.contains_link(cell.neighbor("south")):
                draw.line([x2, y3, x2, y4],
                            fill=wall)
                draw.line([x3, y3, x3, y4],
                            fill=wall)
            else:
                draw.line([x2, y3, x3, y3],
                            fill=wall)
            if cell.contains_link(cell.neighbor("west")):
                draw.line([x1, y2, x2, y2],
                            fill=wall)
                draw.line([x1, y3, x2, y3],
                            fill=wall)
            else:
                draw.line([x2, y2, x2, y3],
                            fill=wall)
            if cell.contains_link(cell.neighbor("east")):
                draw.line([x3, y2, x4, y2],
                            fill=wall)
                draw.line([x3, y3, x4, y3],
                            fill=wall)
            else:
                draw.line([x3, y2, x3, y3],
                            fill=wall)

    def _to_png_without_inset(self, draw, cell, mode, cell_size, wall, x, y):
        x1, y1 = x, y
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        if mode == "background":
            draw.rectangle((x1, y1, x2, y2),
                            fill=self.background_color_for(cell),
                            outline=None,
                            width=0)
        else:
            if cell == None:
                draw.rectangle((x1, y1, x2, y2),
                                fill="black",
                                outline=None,
                                width=0)
            else:
                if not cell.contains_link(cell.neighbor("east")):
                    draw.line([x2, y1, x2, y2],
                                fill=wall)
                if not cell.contains_link(cell.neighbor("south")):
                    draw.line([x1, y2, x2, y2],
                                fill=wall)

