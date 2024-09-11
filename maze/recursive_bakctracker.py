import random

class RecursiveBacktracker:
    def on(grid, start_at=None):
        if not start_at:
            start_at = grid.random_cell()
        stack = []
        stack.append(start_at)

        while len(stack) > 0:
            current = stack[-1]
            neighbors = [cell for cell in current.neighbors()
                         if cell.get_links() == []]
            if len(neighbors) == 0:
                stack.pop()
            else:
                neighbor = random.choice(neighbors)
                current.link(neighbor)
                stack.append(neighbor)
        return grid
