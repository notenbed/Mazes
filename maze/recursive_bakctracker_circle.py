import random

class RecursiveBacktrackerCircle:
    def on(grid, start_at=None):
        if not start_at:
            start_at = grid.random_cell()
        stack = []
        stack.append(start_at)

        while len(stack) > 0:
            current = stack[-1]
            outward_neighbors = []
            if len(current._outward) > 0:
                outward_neighbors = [cell for cell in current._outward
                                     if cell.get_links() == []]
            
            neighbors = [cell for cell in current.neighbors_for_random()
                         if cell != "outward" and cell.get_links() == []]
            if len(neighbors) + len(outward_neighbors) == 0:
                stack.pop()
            else:
                if len(outward_neighbors) > 0:
                    neighbors.append("outward")
                neighbor = random.choice(neighbors)
                if neighbor == "outward":
                    neighbor = random.choice(outward_neighbors)

                current.link(neighbor)
                stack.append(neighbor)
        return grid
