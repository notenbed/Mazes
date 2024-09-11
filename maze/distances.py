class Distances():
    def __init__(self, root):
        self.root = root
        self.cells = {}
        self.cells[root] = 0

    def __getitem__(self, cell):
        if cell in self.cells.keys():
            return self.cells[cell]
        else:
            return None
    
    def __setitem__(self, key, value):
        self.cells[key] = value

    def all_cells(self):
        return list(self.cells.keys())
    
    def path_to(self, goal):
        current = goal

        breadcrumbs = Distances(self.root)
        breadcrumbs[current] = self.cells[current]

        while current != self.root:
            for neighbor in current.links:
               if self.cells[neighbor] < self.cells[current]:
                   breadcrumbs[neighbor] = self.cells[neighbor]
                   current = neighbor
                   break
        return breadcrumbs.cells
    
    def max(self):
        max_distance = 0
        max_cell = self.root

        for key, val in self.cells.items():
            if val > max_distance:
                max_cell = key
                max_distance = val
        
        return [max_cell, max_distance]