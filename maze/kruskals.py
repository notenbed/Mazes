import random
class Kruskals:

    class State:
        def __init__(self, grid):
            self.grid = grid
            self.neighbors = []
            self.set_for_cell = {}
            self.cells_in_set = {}

            for cell in self.grid.each_cell():
                set_cell = len(self.set_for_cell)
                self.set_for_cell[cell] = set_cell
                self.cells_in_set[set_cell] = [cell]

                if cell.neighbor("south") != None: self.neighbors.append([cell, cell.neighbor("south")])
                if cell.neighbor("east") != None: self.neighbors.append([cell, cell.neighbor("east")])

        def merge(self, left, right):
            left.link(right)

            winner = self.set_for_cell[left]
            loser = self.set_for_cell[right] if right in self.set_for_cell else None
            losers = self.cells_in_set[loser] if not(loser == None) else [right] 

            for cell in losers:
                self.cells_in_set[winner].append(cell)
                self.set_for_cell[cell] = winner
            
            if loser != None:
                del self.cells_in_set[loser] 

        def can_merge(self, left, right):
            return self.set_for_cell[left] != self.set_for_cell[right]
        
        def add_crossing(self, cell):
            if (cell.get_links() != [] or
                cell.row == 0 or cell.row == self.grid.rows - 1 or
                cell.column == 0 or cell.column == self.grid.columns - 1 or
                not self.can_merge(cell.neighbor("east"), cell.neighbor("west")) or 
                not self.can_merge(cell.neighbor("north"), cell.neighbor("south"))):
                return False
            
            self.neighbors = [x for x in self.neighbors if not (x[0] == cell or x[1] == cell)]

            if random.randint(0, 1) == 0:
                self.merge(cell.neighbor("west"), cell)
                self.merge(cell, cell.neighbor("east"))

                self.grid.tunnel_under(cell)
                self.merge(cell.neighbor("north"), cell.neighbor("north").neighbor("south"))
                self.merge(cell.neighbor("south"), cell.neighbor("south").neighbor("north"))
            else:
                self.merge(cell.neighbor("north"), cell)
                self.merge(cell, cell.neighbor("south"))

                self.grid.tunnel_under(cell)
                self.merge(cell.neighbor("west"), cell.neighbor("west").neighbor("east"))
                self.merge(cell.neighbor("east"), cell.neighbor("east").neighbor("west"))
            return True



        
    def on(grid, state=None):
        if state == None: state = Kruskals.State(grid)
        random.shuffle(state.neighbors)
        neighbors = state.neighbors
        while len(neighbors) > 0:
            left, right = neighbors.pop()
            if state.can_merge(left, right): state.merge(left, right)
        
        return grid
    
