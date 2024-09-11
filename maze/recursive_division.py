import random
class RecursiveDivision:

    def on(grid):
        def _divide(row, column, height, width):
            # creates large open rooms
            if height <= 1 or width <= 1 or (height < 5 and width < 5 and random.randint(0, 3) == 0): return
#            creates a boxed like structure
#            if height <= 1 or width <= 1: return

            if height > width:
                _divide_horizontally(row, column, height, width)
            else:
                _divide_vertically(row, column, height, width)

        def _divide_horizontally(row, column, height, width):
            divide_south_of = random.randint(0, height-2)
            passage_at = random.randint(0, width-1)

            for x in range(0, width):
                if passage_at == x: continue

                cell = grid[row+divide_south_of, column+x]
                cell.unlink(cell.neighbor("south"))
            _divide(row, column, divide_south_of+1, width)
            _divide(row+divide_south_of+1, column, height-divide_south_of-1, width)

        def _divide_vertically(row, column, height, width):
            divide_east_of = random.randint(0, width-2)
            passage_at = random.randint(0, height-1)

            for y in range(0, height):
                if passage_at == y: continue

                cell = grid[row+y, column+divide_east_of]
                cell.unlink(cell.neighbor("east"))

            _divide(row, column, height, divide_east_of+1)
            _divide(row, column+divide_east_of+1, height, width-divide_east_of-1)

        for cell in grid.each_cell():
            for neighbor in cell.neighbors():
                if not cell.contains_link(neighbor):
                    cell.link(neighbor)
        _divide(0, 0, grid.rows, grid.columns)

