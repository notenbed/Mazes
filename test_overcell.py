from maze import OverCell
from maze import UnderCell
from maze import WeaveGrid

def test_neighbors():
    grid = WeaveGrid(6, 6)

    assert grid[1, 2].neighbors() == [grid[0, 2], grid[2, 2], grid[1, 3], grid[1, 1]]
    
    # create horizontal passage
    grid[2, 1].link(grid[2, 2])
    grid[2, 2].link(grid[2, 3])

    assert grid[2, 0].neighbors() == [grid[1, 0], grid[3, 0], grid[2, 1]]
    assert grid[1, 2].neighbors() == [grid[0, 2], grid[2, 2], grid[1, 3], grid[1, 1], grid[3, 2]]

    # create vertical passage
    grid[3, 4].link(grid[4, 4])
    grid[4, 4].link(grid[5, 4])

    assert grid[4, 3].neighbors() == [grid[3, 3], grid[5, 3], grid[4, 4], grid[4, 2], grid[4, 5]]

def test_create_undercell():
    grid = WeaveGrid(6, 6)

    # create horizontal passage
    grid[2, 1].link(grid[2, 2])
    grid[2, 2].link(grid[2, 3])

    grid[1, 2].link(grid[3, 2])

    assert isinstance(grid[1, 2].neighbor("south"), UnderCell)
    assert isinstance(grid[3, 2].neighbor("north"), UnderCell)
    assert grid.under_cells == [grid[1, 2].neighbor("south")]
    assert grid[1, 2].neighbor("south").neighbor("north") == grid[1, 2]
    assert grid[1, 2].neighbor("south").neighbor("south") == grid[3, 2]
    assert grid[1, 2].neighbor("south").get_links() == [grid[1, 2], grid[3, 2]]

    #create vertical passage
    grid[3, 4].link(grid[4, 4])
    grid[4, 4].link(grid[5, 4])

    grid[4, 3].link(grid[4, 5])

    assert isinstance(grid[4, 3].neighbor("east"), UnderCell)
    assert isinstance(grid[4, 5].neighbor("west"), UnderCell)
    assert grid.under_cells == [grid[1, 2].neighbor("south"), grid[4, 3].neighbor("east")]
    assert grid[4, 3].neighbor("east").neighbor("west") == grid[4, 3]
    assert grid[4, 3].neighbor("east").neighbor("east") == grid[4, 5]
    assert grid[4, 3].neighbor("east").get_links() == [grid[4, 5], grid[4, 3]]
