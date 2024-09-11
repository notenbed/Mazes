import random

class BinaryTree:
    def on(grid):
        for cell in grid.each_cell():
            neighbors = []
            if cell.neighbor("north"):
                neighbors.append(cell.neighbor("north"))
            if cell.neighbor("east"):
                neighbors.append(cell.neighbor("east"))
            if len(neighbors) > 0:
                cell.link(random.choice(neighbors))
        return grid
    
            