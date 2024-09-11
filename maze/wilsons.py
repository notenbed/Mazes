import random

class Wilsons:

# It does not do the job!
# It creates lot of small isolated paths that are not connected.    
    def on(grid):
        unvisited = [cell for cell in grid.each_cell()]
        first = random.choice(unvisited)
        unvisited.remove(first)
        while len(unvisited) != 0:
            cell = random.choice(unvisited)
            path = [cell]
            while cell in unvisited:
                cell = cell.random_neighbor()
                if cell in path:
                    position = path.index(cell)
                    path = path[0:position]
                else:
                    path.append(cell)

            for index in range(0, len(path) - 1):
                path[index].link(path[index + 1])
                if path[index] in unvisited:
                    unvisited.remove(path[index])
        return grid