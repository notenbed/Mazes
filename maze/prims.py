import random

class SimplifiedPrims:
    
    def on(grid, start_at=None):
        if start_at == None: start_at = grid.random_cell()

        active = []
        active.append(start_at)

        while len(active) != 0:
            cell = random.choice(active)
            available_neighbors = [neighbor for neighbor in cell.neighbors() if neighbor.get_links() == []]

            if len(available_neighbors) != 0:
                neighbor = random.choice(available_neighbors)
                cell.link(neighbor)
                active.append(neighbor)
            else:
                active.remove(cell)

        return grid
    
class TruePrims:

    def on(grid, start_at=None):
        def _minimum_cost_cell(cells, costs):
            minimum = float('inf')
            min_cells = []
            for cell in cells:
                if costs[cell] <= minimum:
                    minimum = costs[cell]
                    min_cells.append(cell)
            return random.choice(min_cells)        
        
        if start_at == None: start_at = grid.random_cell()

        active = []
        active.append(start_at)

        costs = dict.fromkeys([cell for cell in grid.each_cell()], random.randint(1, 100))

        while len(active) != 0:
            cell = _minimum_cost_cell(active, costs)
            available_neighbors = [neighbor for neighbor in cell.neighbors() if neighbor.get_links() == []]

            if len(available_neighbors) != 0:
                neighbor = _minimum_cost_cell(available_neighbors, costs)
                cell.link(neighbor)
                active.append(neighbor)
            else:
                active.remove(cell)
        return grid
    
