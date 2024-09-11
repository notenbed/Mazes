from maze import Cell

class OverCell(Cell):
    def __init__(self,row, column, grid):
        super().__init__(row, column)
        self.grid = grid

    def neighbors(self):
        neighbor_list = super().neighbors()

        if self._can_tunnel_north(): neighbor_list.append(self.neighbor("north").neighbor("north"))
        if self._can_tunnel_south(): neighbor_list.append(self.neighbor("south").neighbor("south"))
        if self._can_tunnel_east(): neighbor_list.append(self.neighbor("east").neighbor("east"))
        if self._can_tunnel_west(): neighbor_list.append(self.neighbor("west").neighbor("west"))

        return neighbor_list

    def _can_tunnel_north(self):
        north = self.neighbor("north")
        return north != None and north.neighbor("north") != None and north.horizontal_passage()

    def _can_tunnel_south(self):
        south = self.neighbor("south")
        return south != None and south.neighbor("south") != None and south.horizontal_passage()
    
    def _can_tunnel_west(self):
        west = self.neighbor("west")
        return west != None and west.neighbor("west") != None and west.vertical_passage()
    
    def _can_tunnel_east(self):
        east = self.neighbor("east")
        return east != None and east.neighbor("east") != None and east.vertical_passage()
    
    def horizontal_passage(self):
        return (self.neighbor("east") in self.links and 
                self.neighbor("west") in self.links and 
                self.neighbor("north") not in self.links and 
                self.neighbor("south") not in self.links)

    def vertical_passage(self):
        return (self.neighbor("north") in self.links and
                self.neighbor("south") in self.links and
                self.neighbor("east") not in self.links and
                self.neighbor("west") not in self.links)
    
    def link(self, cell, bidi=True):
        neighbor = None
        if self.neighbor("north") and self.neighbor("north") == cell.neighbor("south"):
            neighbor = self.neighbor("north")
        elif self.neighbor("south") and self.neighbor("south") == cell.neighbor("north"):
            neighbor = self.neighbor("south")
        elif self.neighbor("east") and self.neighbor("east") == cell.neighbor("west"):
            neighbor = self.neighbor("east")
        elif self.neighbor("west") and self.neighbor("west") == cell.neighbor("east"):
            neighbor = self.neighbor("west")

        if neighbor != None:
            self.grid.tunnel_under(neighbor)
        else:
            super().link(cell, bidi=True)

class UnderCell(Cell):
    def __init__(self, over_cell):
        super().__init__(over_cell.row, over_cell.column)

        if over_cell.horizontal_passage():
            self.add_neighbor("north", over_cell.neighbor("north"))
            over_cell.neighbor("north").add_neighbor("south", self)
            self.add_neighbor("south", over_cell.neighbor("south"))
            over_cell.neighbor("south").add_neighbor("north", self)
            self.link(self.neighbor("north"))
            self.link(self.neighbor("south"))
        else:
            self.add_neighbor("east", over_cell.neighbor("east"))
            over_cell.neighbor("east").add_neighbor("west", self)
            self.add_neighbor("west", over_cell.neighbor("west"))
            over_cell.neighbor("west").add_neighbor("east", self)
            self.link(self.neighbor("east"))
            self.link(self.neighbor("west"))

    def horizontal_passage(self):
        return self.neighbor("east") != None or self.neighbor("west") != None

    def vertical_passage(self):
        return self.neighbor("north") != None or self.neighbor("south") != None
    