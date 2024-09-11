import random

class GrowingTree:
    
    def on(block, grid, start_at=None):
        if start_at == None: start_at = grid.random_cell()

        active = []
        active.append(start_at)

        while len(active) != 0:
            cell = block(active)
            available_neighbors = [neighbor for neighbor in cell.neighbors() if neighbor.get_links() == []]
            if len(available_neighbors) != 0:
                neighbor = random.choice(available_neighbors)
                cell.link(neighbor)
                active.append(neighbor)
            else:
                active.remove(cell)
        
        return grid
