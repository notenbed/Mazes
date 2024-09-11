import random

class Sidewinder:
    
    def on(grid):
        for row in grid.each_row():
            run = []
            for cell in row:
                run.append(cell)
                at_eastern_boundary =  not cell.neighbor("east")
                at_northern_boundary = not cell.neighbor("north")
                should_close_out = at_eastern_boundary or (not(at_northern_boundary) and random.randint(0, 2) == 0)

                if should_close_out:
                    member = random.choice(run)
                    if member.neighbor("north"): member.link(member.neighbor("north"))
                    run = []
                else:
                    cell.link(cell.neighbor("east"))
        return grid
    
