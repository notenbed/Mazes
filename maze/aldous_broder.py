class AldousBroder:
    def on(grid):
        cell = grid.random_cell()
        unvisited = grid.size() - 1

        while unvisited > 0:
            neighbor = cell.random_neighbor()

            if neighbor.links == []:
                cell.link(neighbor)
                unvisited -= 1
            
            cell = neighbor

        return grid
