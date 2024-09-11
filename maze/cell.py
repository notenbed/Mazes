from maze import Distances
import random

class Cell():
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = []
        self._neighbors = dict()
    
    def neighbor(self, key):
        return self._neighbors[key] if key in self._neighbors else None
        
    def each_neighbor(self):
        for neighbor in self._neighbors.values():
            yield neighbor

    def neighbors(self):
        neighbor_list = []
        if self.neighbor("north"): neighbor_list.append(self.neighbor("north"))
        if self.neighbor("south"): neighbor_list.append(self.neighbor("south"))
        if self.neighbor("east"): neighbor_list.append(self.neighbor("east"))
        if self.neighbor("west"): neighbor_list.append(self.neighbor("west"))
        return neighbor_list
    
    def remove_neighbor(self, key):
        self._neighbors.pop(key)
        
    def add_neighbor(self, key, value):
        self._neighbors[key] = value
    
    def random_neighbor(self):
        selection = random.choice(list(self._neighbors.keys()))
        return self.neighbor(selection)

    def link(self, cell, bidi=True):
        if cell != "":
            self.links.append(cell)
            if bidi: cell.links.append(self)

    def unlink(self, cell, bidi=True):
        self.links.remove(cell)
        if bidi: cell.links.remove(self)
    
    def get_links(self):
        return self.links
    
    def contains_link(self, cell):
        return cell in self.links
    
    def distances(self):
        distances = Distances(self)
        frontier = [self]
        while len(frontier) > 0:
            new_frontier = []
            for front in frontier:

                for cell in front.get_links():
                    if cell not in distances.cells:
                        distances[cell] = distances[front] + 1
                        new_frontier.append(cell)
            frontier = new_frontier
        return distances
