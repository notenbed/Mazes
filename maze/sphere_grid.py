from maze import Grid
from maze import PolarGrid
from maze import HemisphereCell
import math
import random
from PIL import Image, ImageDraw

class HemisphereGrid(PolarGrid):
    def __init__(self, id, rows):
        self.id = id
        super().__init__(rows)

    def size(self, row):
        return len(self[row])
    
    def _prepare_grid(self):
        maze = []
        angular_height = math.pi / (2 * self.rows)

        maze.append([HemisphereCell(self.id, 0, 0)])
        for row in range(1, self.rows):
            theta = (row + 1) * angular_height
            radius = math.sin(theta)
            circumference = 2 * math.pi * radius

            previous_count = len(maze[row - 1])
            estimated_cell_width = circumference / previous_count
            ratio = round(estimated_cell_width / angular_height)
            
            cells = int(previous_count * ratio)
            maze.append([HemisphereCell(self.id, row, col) for col in range(0, cells)])

        return maze

class SphereGrid(Grid):
    def __init__(self, rows):
        if rows % 2 == 1:
            raise Exception("argument must be an even number")
        self.equator = round(rows / 2)
        super().__init__(rows, 1)

    def _prepare_grid(self):
        maze = [HemisphereGrid(id, self.equator) for id in [0, 1]]
        return maze
    
    def __getitem__(self, x):
        return self.grid[x[0]][x[1], x[2]]
    
    def _configure_cells(self):
        belt = self.equator - 1
        for index in range(0, self.size(belt)):
            a, b = self[0, belt, index], self[1, belt, index]
            a.extend_outward_neighbors(b)
            b.extend_outward_neighbors(a)

    def size(self, row):
        hemi = self.grid[0]
        return len(hemi.grid[row])
    
    def each_cell(self):
        for hemi in self.grid:
            for cell in hemi.each_cell():
                yield cell

    def random_cell(self):
        hemi = random.choice([0, 1])
        return self.grid[hemi].random_cell()
    
    def to_img(self, ideal_size=10, filename="grid.png"):
        img_height = ideal_size * self.rows
        img_width = int(self.size(self.equator - 1) * ideal_size)

        background = "white"
        wall = "black"

        img = Image.new(
            "RGBA",
            (img_width + 1, img_height + 1),
            "white"
            )
        draw = ImageDraw.Draw(img)

        for cell in self.each_cell():
            row_size = self.size(cell.row)
            cell_width = img_width / row_size

            x1 = cell.column * cell_width
            x2 = x1 + cell_width

            y1 = cell.row * ideal_size
            y2 = y1 + ideal_size

            if cell.hemisphere > 0:
                y1 = img_height - y1
                y2 = img_height - y2
            
            x1 = round(x1)
            y1 = round(y1)
            x2 = round(x2)
            y2 = round(y2)

            if cell.row > 0:
                if not cell.contains_link(cell.neighbor("cw")): draw.line([x2, y1, x2, y2],
                          fill=wall)
                if not cell.contains_link(cell.neighbor("inward")): draw.line([x1, y1, x2, y1],
                          fill=wall)
                    
            if cell.hemisphere == 0 and cell.row == self.equator - 1:
                if not cell.contains_link(cell.neighbor("outward")[0]): draw.line([x1, y2, x2, y2],
                          fill=wall)
                    
        img.save(filename)
