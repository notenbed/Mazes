from maze import Grid

def test_initialize_grid():
    g = Grid(4, 5)
    assert len(g.grid) == 4
    assert len(g.grid[0]) == 5

def test_configure_cells():
    grid = Grid(4, 5)
    assert grid[0, 0].neighbor("east") == grid[0, 1]
    assert grid[0, 0].neighbor("south") == grid[1, 0]
    assert grid[1, 0].neighbor('north') == grid[0, 0]
    assert grid[0, 1].neighbor("west") == grid[0, 0]
    assert grid[0, 4].neighbor("east") == None
    assert grid[3, 0].neighbor("south") == None
    assert grid[0, 0].neighbor("north") == None
    assert grid[0, 0].neighbor("west") == None

def test_grid_size():
    g = Grid(4, 5)
    assert g.size() == 20

def test_each_row():
    g = Grid(2, 1)
    assert list(g.each_row()) == [g.grid[0], g.grid[1]]

def test_each_cell():
    grid = Grid(2, 2)
    assert list(grid.each_cell()) == [grid[0, 0], grid[0, 1], grid[1, 0], grid[1, 1]]

def test_get_item():
    g = Grid(2, 3)
    assert g[0, 1] == g.grid[0][1]