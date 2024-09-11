import random

class Ellers:

    class RowState:
        def __init__(self, starting_set=0):
            self.cells_in_set = {}
            self.set_for_cell = {}
            self.next_set = starting_set
        
        def record(self, set, cell):
            self.set_for_cell[cell.column] = set

            if set not in self.cells_in_set: self.cells_in_set[set] = []
            self.cells_in_set[set].append(cell)

        def set_for(self, cell):
            if cell.column not in self.set_for_cell.keys():
                self.record(self.next_set, cell)
                self.next_set += 1
            
            return self.set_for_cell[cell.column]
        
        def merge(self, winner, loser):
            for cell in self.cells_in_set[loser]:
                self.set_for_cell[cell.column] = winner
                self.cells_in_set[winner].append(cell)

            del self.cells_in_set[loser]
        
        def next(self):
            return Ellers.RowState(self.next_set)
        
        def each_set(self):
            for set, cell in self.cells_in_set.items():
                yield set, cell
    
    def on(grid):
        row_state = Ellers.RowState()

        for row in grid.each_row():
            for cell in row:
                if cell.neighbor("west") == None:
                    continue
                
                
                cell_set = row_state.set_for(cell)
                prior_set = row_state.set_for(cell.neighbor("west"))

                if prior_set != cell_set and (cell.neighbor("south") == 0 or random.randint(0, 2) == 0):
                    cell.link(cell.neighbor("west"))
                    row_state.merge(prior_set, cell_set)
            
            if row[0].neighbor("south"):
                next_row = row_state.next()

                for set, cell_list in row_state.each_set():
                    random.shuffle(cell_list)
                    for index, cell in [(index, cell) for index, cell in enumerate(cell_list)]:
                        if index == 0 or random.randint(0, 2):
                            cell.link(cell.neighbor("south"))
                            next_row.record(row_state.set_for(cell), cell.neighbor("south"))
                row_state = next_row