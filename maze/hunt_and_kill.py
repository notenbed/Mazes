import random

class HuntAndKill:
    def on(grid):
        current = grid.random_cell()

        while current:
            unvisited_neighbors = [cell for cell in current.each_neighbor() 
                                   if cell.get_links() == []]
            if unvisited_neighbors != []:
                neighbor = random.choice(unvisited_neighbors)
                current.link(neighbor)
                current = neighbor
            else:
                current = None

                for cell in grid.each_cell():
                    visited_neighbors = [x for x in cell.each_neighbor() 
                                         if x.get_links() != []]
                    if cell.links == [] and visited_neighbors != []:
                        current = cell
                        neighbor = random.choice(visited_neighbors)
                        current.link(neighbor)
                        break
        return grid            